from typing import Dict, List, Optional
from web3 import Web3
from slither import Slither
from slither.analyses.data_dependency.data_dependency import is_dependent
from app.utils.exceptions import AnalysisError
import os

# Static analysis of Ethereum smart contracts using Slither
class ContractAnalyzer:
    """
    Smart contract analyzer using Slither and custom checks.
    Performs static analysis and vulnerability detection.
    """
    
    def __init__(self, web3_provider: Optional[Web3] = None):
        """Initialize analyzer with optional Web3 provider."""
        self.web3 = web3_provider or Web3(Web3.HTTPProvider(
            f"https://mainnet.infura.io/v3/{os.getenv('INFURA_PROJECT_ID')}"
        ))

    async def analyze(self, contract_address: str) -> Dict:
        """
        Analyze smart contract for vulnerabilities and patterns.
        
        Args:
            contract_address (str): Ethereum contract address
            
        Returns:
            Dict: Analysis results including vulnerabilities and metrics
            
        Raises:
            AnalysisError: If analysis fails
        """
        try:
            # Initialize Slither with the contract address
            slither = Slither(contract_address)
            
            # Collect analysis results
            results = {
                "vulnerabilities": self._check_vulnerabilities(slither),
                "metrics": self._collect_metrics(slither),
                "gas_analysis": self._analyze_gas_usage(slither),
                "dependencies": self._check_dependencies(slither),
                "risk_score": self._calculate_risk_score(slither)
            }
            
            return results
            
        except Exception as e:
            raise AnalysisError(f"Analysis failed: {str(e)}")

    def _check_vulnerabilities(self, slither: Slither) -> Dict:
        """Check for common vulnerabilities."""
        vulnerabilities = {
            "reentrancy": [],
            "integer_overflow": [],
            "unprotected_functions": [],
            "tx_origin": [],
            "unchecked_calls": [],
            "arbitrary_send": []
        }

        for contract in slither.contracts:
            for function in contract.functions:
                # Reentrancy check
                if function.is_reentrant:
                    vulnerabilities["reentrancy"].append(function.name)
                
                # Unprotected function check
                if function.visibility in ["public", "external"] and not function.is_protected():
                    vulnerabilities["unprotected_functions"].append(function.name)
                
                # tx.origin check
                if any(tx_origin in str(node) for node in function.nodes):
                    vulnerabilities["tx_origin"].append(function.name)
                
                # Unchecked external calls
                if function.has_external_calls and not function.has_return_value_test:
                    vulnerabilities["unchecked_calls"].append(function.name)

        return vulnerabilities

    def _collect_metrics(self, slither: Slither) -> Dict:
        """Collect contract metrics."""
        metrics = {
            "total_functions": 0,
            "public_functions": 0,
            "external_functions": 0,
            "state_variables": 0,
            "complexity_score": 0
        }

        for contract in slither.contracts:
            metrics["total_functions"] += len(contract.functions)
            metrics["public_functions"] += len([f for f in contract.functions if f.visibility == "public"])
            metrics["external_functions"] += len([f for f in contract.functions if f.visibility == "external"])
            metrics["state_variables"] += len(contract.state_variables)
            
            # Calculate complexity score
            for function in contract.functions:
                metrics["complexity_score"] += len(function.nodes)

        return metrics

    def _analyze_gas_usage(self, slither: Slither) -> Dict:
        """Analyze potential gas usage issues."""
        gas_analysis = {
            "high_gas_patterns": [],
            "optimization_suggestions": []
        }

        for contract in slither.contracts:
            for function in contract.functions:
                # Check for loops over arrays
                if any("for" in str(node) for node in function.nodes):
                    gas_analysis["high_gas_patterns"].append(
                        f"Loop in {function.name}: Consider pagination"
                    )
                
                # Check for multiple external calls
                if len(function.external_calls) > 2:
                    gas_analysis["high_gas_patterns"].append(
                        f"Multiple external calls in {function.name}: Consider batching"
                    )

        return gas_analysis

    def _check_dependencies(self, slither: Slither) -> List[str]:
        """Check contract dependencies and inherited contracts."""
        dependencies = []
        
        for contract in slither.contracts:
            for inherited in contract.inheritance:
                dependencies.append(f"Inherits from: {inherited.name}")
            
            for called_contract in contract.high_level_calls:
                dependencies.append(f"Calls contract: {called_contract.name}")

        return dependencies

    def _calculate_risk_score(self, slither: Slither) -> int:
        """Calculate overall risk score based on findings."""
        risk_score = 0
        
        # Analyze vulnerabilities
        for contract in slither.contracts:
            if any(f.is_reentrant for f in contract.functions):
                risk_score += 30
            
            if any(not f.is_protected() for f in contract.functions if f.visibility in ["public", "external"]):
                risk_score += 20
            
            if len(contract.external_calls) > 5:
                risk_score += 10

        return min(risk_score, 100)  # Cap at 100