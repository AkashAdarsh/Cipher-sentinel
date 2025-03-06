from fastapi import FastAPI, HTTPException
from app.models.audit import AuditRequest
from app.services.ethereum import fetch_contract_bytecode
from app.utils.logging import setup_logger

logger = setup_logger()
app = FastAPI()

@app.get("/health")
async def health_check():
    logger.info("Health check endpoint called")
    return {"status": "ok"}

@app.post("/audit")
async def audit_contract(request: AuditRequest):
    logger.info(f"Audit request received for contract: {request.contract_address}")
    
    try:
        bytecode = fetch_contract_bytecode(request.contract_address)
        
        if bytecode == "0x":
            logger.error(f"No bytecode found for contract: {request.contract_address}")
            raise HTTPException(status_code=400, detail="Contract not found or has no bytecode")
        
        logger.info(f"Bytecode fetched for contract: {request.contract_address}")
        return {
            "contract_address": request.contract_address,
            "audit_status": "pending_analysis",
            "bytecode_length": len(bytecode)
        }
        
    except Exception as e:
        logger.error(f"Error fetching contract data: {e}")
        raise HTTPException(status_code=500, detail="Error fetching contract data")

# Ethereum connection check (optional)
if __name__ == "__main__":
    from app.services.ethereum import get_web3_provider
    web3 = get_web3_provider()
    if web3.is_connected():
        logger.info("Connected to Ethereum network")
    else:
        logger.error("Failed to connect to Ethereum network")