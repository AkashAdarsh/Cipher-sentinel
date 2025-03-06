from web3 import Web3
from dotenv import load_dotenv
import os

load_dotenv()

def get_web3_provider():
    infura_url = f"https://goerli.infura.io/v3/{os.getenv('INFURA_PROJECT_ID')}"
    return Web3(Web3.HTTPProvider(infura_url))

def fetch_contract_bytecode(contract_address):
    web3 = get_web3_provider()
    return web3.eth.get_code(contract_address)