from pydantic import BaseModel, validator, Field
from web3 import Web3
from typing import Optional

# Pydantic model for validating audit requests
class AuditRequest(BaseModel):
    """
    Contract audit request model.
    
    Attributes:
        contract_address (str): Ethereum contract address to analyze
        chain_id (int): Ethereum chain ID (1 for mainnet, 5 for goerli)
        analysis_depth (str): Depth of analysis (basic, standard, or deep)
    """
    contract_address: str = Field(..., description="Ethereum contract address to analyze")
    chain_id: int = Field(default=1, description="Ethereum chain ID (1=mainnet, 5=goerli)")
    analysis_depth: str = Field(
        default="standard",
        description="Depth of analysis to perform"
    )

    @validator("contract_address")
    def validate_contract_address(cls, value: str) -> str:
        """Validate Ethereum contract address."""
        if not Web3.is_address(value):
            raise ValueError("Invalid Ethereum address format")
        return Web3.to_checksum_address(value)

    @validator("chain_id")
    def validate_chain_id(cls, value: int) -> int:
        """Validate Ethereum chain ID."""
        valid_chains = {
            1: "mainnet",
            5: "goerli",
            11155111: "sepolia"
        }
        if value not in valid_chains:
            raise ValueError(f"Invalid chain ID. Supported chains: {valid_chains}")
        return value

    @validator("analysis_depth")
    def validate_analysis_depth(cls, value: str) -> str:
        """Validate analysis depth option."""
        valid_depths = ["basic", "standard", "deep"]
        if value.lower() not in valid_depths:
            raise ValueError(f"Invalid analysis depth. Must be one of: {valid_depths}")
        return value.lower()

    class Config:
        json_schema_extra = {
            "example": {
                "contract_address": "0x742d35Cc6634C0532925a3b844Bc454e4438f44e",
                "chain_id": 1,
                "analysis_depth": "standard"
            }
        }