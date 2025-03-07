from celery import Celery
from app.services.ethereum import fetch_contract_bytecode
from app.services.analyzer import ContractAnalyzer

celery = Celery(__name__, broker='redis://localhost:6379/0')

@celery.task
def run_audit_task(contract_address: str):
    try:
        bytecode = fetch_contract_bytecode(contract_address)
        analysis = ContractAnalyzer.analyze(contract_address)
        
        return {
            "contract_address": contract_address,
            "bytecode_length": len(bytecode),
            "vulnerabilities": analysis
        }
        
    except Exception as e:
        return {"error": str(e)}