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


def test_request_without_content_length_passes() -> None:
    """Test that the absence of a Content-Length header does not block the request."""
    # A standard GET request without body has no Content-Length
    response = client.get("/health")
    
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_custom_max_upload_size(monkeypatch) -> None:
    """
    Test that the upload limit is properly loaded and enforced from the environment variable.
    We instantiate a local mock app because the global 'app' has already evaluated os.getenv
    during its import, making monkeypatch ineffective on it.
    """
    monkeypatch.setenv("API_MAX_UPLOAD_SIZE", "100")
    
    from fastapi import FastAPI
    from {{ cookiecutter.package_name }}.api.middlewares import LimitUploadSizeMiddleware
    
    test_app = FastAPI()
    test_app.add_middleware(LimitUploadSizeMiddleware)
    
    @test_app.post("/test")
    def test_route():
        return {"status": "ok"}
        
    local_client = TestClient(test_app)
    
    # 200 bytes > 100 bytes limit
    response = local_client.post("/test", headers={"content-length": "200"})
    assert response.status_code == 413

