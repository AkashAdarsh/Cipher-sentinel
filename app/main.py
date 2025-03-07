from fastapi import FastAPI
from celery import Celery
from app.models.audit import AuditRequest
from app.services.ethereum import fetch_contract_bytecode
from app.services.analyzer import ContractAnalyzer
from app.utils.logging import setup_logger
from app.utils.exceptions import AuditException
from app.tasks.audit_tasks import run_audit_task

logger = setup_logger()
app = FastAPI()

# Celery configuration
celery = Celery(
    __name__,
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

@app.get("/health")
async def health_check():
    logger.info("Health check endpoint called")
    return {"status": "ok", "version": "0.4"}

@app.post("/audit")
async def audit_contract(request: AuditRequest):
    logger.info(f"Audit request received for contract: {request.contract_address}")
    
    try:
        # Fetch bytecode
        bytecode = fetch_contract_bytecode(request.contract_address)
        
        # Start async analysis
        task = run_audit_task.delay(request.contract_address)
        
        return {
            "contract_address": request.contract_address,
            "task_id": task.id,
            "status": "analysis_started"
        }
        
    except Exception as e:
        logger.error(f"Audit failed: {str(e)}")
        raise AuditException(detail=str(e))