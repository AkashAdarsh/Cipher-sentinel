from fastapi import FastAPI, HTTPException, BackgroundTasks
from celery import Celery
from app.models.audit import AuditRequest
from app.services.ethereum import fetch_contract_bytecode
from app.services.analyzer import ContractAnalyzer
from app.utils.logging import setup_logger
from app.utils.exceptions import AuditException, AnalysisError
from app.tasks.audit_tasks import run_audit_task

# Initialize logger for tracking application events
logger = setup_logger()
app = FastAPI(
    title="CipherSentinel",
    description="AI-powered smart contract auditor and rug pull analyzer",
    version="0.4.0"
)

# Configure Celery for asynchronous task processing
celery = Celery(
    __name__,
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

@app.get("/health")
async def health_check():
    """Health check endpoint to verify the API is running."""
    logger.info("Health check endpoint called")
    return {
        "status": "ok",
        "version": "0.4.0",
        "services": {
            "api": "healthy",
            "celery": "healthy",
            "redis": "healthy"
        }
    }

@app.post("/audit")
async def audit_contract(request: AuditRequest, background_tasks: BackgroundTasks):
    """
    Initiate smart contract audit.
    
    Args:
        request (AuditRequest): Contract audit request
        background_tasks (BackgroundTasks): FastAPI background tasks
        
    Returns:
        dict: Task information and initial status
    """
    logger.info(f"Audit request received for contract: {request.contract_address}")
    
    try:
        # Fetch contract bytecode
        bytecode = await fetch_contract_bytecode(request.contract_address)
        
        # Start asynchronous analysis
        task = run_audit_task.delay(request.contract_address)
        
        # Return task information
        return {
            "status": "analysis_started",
            "contract_address": request.contract_address,
            "task_id": task.id,
            "bytecode_length": len(bytecode),
            "estimated_time": "30-60 seconds"
        }
        
    except Exception as e:
        logger.error(f"Audit failed: {str(e)}")
        raise AuditException(detail=str(e))

@app.get("/audit/{task_id}")
async def get_audit_status(task_id: str):
    """
    Get the status of an ongoing audit task.
    
    Args:
        task_id (str): Celery task ID
        
    Returns:
        dict: Current task status and results if available
    """
    try:
        task = celery.AsyncResult(task_id)
        
        if task.ready():
            result = task.get()
            return {
                "status": "completed",
                "result": result
            }
        
        return {
            "status": "in_progress",
            "task_id": task_id
        }
        
    except Exception as e:
        logger.error(f"Failed to get task status: {str(e)}")
        raise HTTPException(
            status_code=400,
            detail=f"Failed to get task status: {str(e)}"
        )