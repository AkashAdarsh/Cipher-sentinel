from pydantic import BaseModel, validator
from web3 import Web3

class AuditRequest(BaseModel):
    contract_address: str

    @validator("contract_address")
    def validate_contract_address(cls, value):
        if not Web3.is_address(value):
            raise ValueError("Invalid Ethereum address")
        return Web3.to_checksum_address(value)