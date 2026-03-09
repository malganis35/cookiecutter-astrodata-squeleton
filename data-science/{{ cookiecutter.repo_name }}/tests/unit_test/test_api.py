import pytest
from fastapi.testclient import TestClient
from {{ cookiecutter.package_name }}.api.main import app

client = TestClient(app)

def test_health_endpoint():
    """Tests the /health endpoint for a 200 status."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_api_home():
    """Tests the root API route."""
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome to my API!" in response.json()["message"]

def test_api_hello():
    """Tests the /hello route defined in routes.py."""
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world!"}

def test_api_bonjour():
    """Tests the /bonjour route defined in routes.py."""
    response = client.get("/bonjour")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world!"}