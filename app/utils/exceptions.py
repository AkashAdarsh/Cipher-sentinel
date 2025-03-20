from fastapi import HTTPException
# Custom exception for audit-related errors
class AuditException(HTTPException):
    """Exception raised for audit-related errors."""
    def __init__(self, detail: str):
        super().__init__(
            status_code=400,
            detail=f"Audit failed: {detail}",
        )

class AnalysisError(HTTPException):
    """Exception raised for contract analysis errors."""
    def __init__(self, detail: str):
        super().__init__(
            status_code=400,
            detail=f"Analysis failed: {detail}",
        )