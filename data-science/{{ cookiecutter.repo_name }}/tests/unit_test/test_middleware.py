"""Unit tests for FastAPI middlewares."""

from fastapi.testclient import TestClient

from {{ cookiecutter.package_name }}.api.main import app

client = TestClient(app)


def test_large_request_rejected() -> None:
    """Test that requests with a Content-Length exceeding the limit are rejected with 413."""
    # Simulation of an oversized payload (e.g. almost 1 GB)
    response = client.post("/health", headers={"content-length": "999999999"})
    
    assert response.status_code == 413
    assert "Request entity too large" in response.json()["detail"]


def test_normal_request_passes() -> None:
    """Test that regular requests without massive payloads pass through normally."""
    response = client.get("/health")
    
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
