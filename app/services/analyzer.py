from slither import Slither

class ContractAnalyzer:
    @staticmethod
    def analyze(contract_address: str) -> dict:
        try:
            slither = Slither(contract_address)
            results = {
                "reentrancy": False,
                "integer_overflow": False,
                "unprotected_function": False
            }

            # Check for reentrancy
            for contract in slither.contracts:
                for function in contract.functions:
                    if function.is_reentrant:
                        results["reentrancy"] = True
                    if function.visibility in ["public", "external"] and not function.is_protected():
                        results["unprotected_function"] = True

            return results
            
        except Exception as e:
            return {"error": str(e)}