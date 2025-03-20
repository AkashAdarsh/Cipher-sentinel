from web3 import Web3
import os

# Initialize Web3 provider using Infura
def get_web3_provider():
    infura_url = f"https://goerli.infura.io/v3/{os.getenv('78103f1f9bba4b0f91b13729d0c15321')}"
    return Web3(Web3.HTTPProvider(infura_url))

# Fetch contract bytecode from Ethereum
def fetch_contract_bytecode(contract_address: str):
    web3 = get_web3_provider()
    bytecode = web3.eth.get_code(contract_address)
    # Validate that the contract exists and has bytecode
    if bytecode == "0x":
        raise ValueError("Contract not found or has no bytecode")
        
    return bytecode