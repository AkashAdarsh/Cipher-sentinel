from celery import Celery
from app.services.ethereum import fetch_contract_bytecode
from app.services.analyzer import ContractAnalyzer
from app.utils.exceptions import AnalysisError
from datetime import datetime

# Initialize Celery application
celery = Celery(
    __name__,
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

@celery.task(bind=True, max_retries=3)
async def run_audit_task(self, contract_address: str):
    """
    Celery task for asynchronous contract analysis.
    
    Args:
        contract_address (str): Ethereum contract address to analyze
        
    Returns:
        dict: Analysis results including vulnerabilities and metrics
    """
    try:
        # Fetch contract bytecode
        bytecode = await fetch_contract_bytecode(contract_address)
        
        # Initialize analyzer
        analyzer = ContractAnalyzer()
        
        # Perform analysis
        analysis_results = await analyzer.analyze(contract_address)
        
        # Return comprehensive results
        return {
            "status": "completed",
            "contract_address": contract_address,
            "bytecode_length": len(bytecode),
            "analysis": analysis_results,
            "timestamp": datetime.utcnow().isoformat()
        }
        
    except Exception as e:
        # Retry on failure
        if self.request.retries < self.max_retries:
            raise self.retry(exc=e, countdown=2 ** self.request.retries)
        
        return {
            "status": "failed",
            "contract_address": contract_address,
            "error": str(e),
            "timestamp": datetime.utcnow().isoformat()
        }