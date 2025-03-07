from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["version"] == "0.4"

def test_audit_endpoint():
    response = client.post("/audit", json={
        "contract_address": "0x0000000000000000000000000000000000000000"
    })
    assert response.status_code == 400  # Expected invalid address error