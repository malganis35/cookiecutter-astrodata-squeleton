"""Unit tests for the FastAPI application endpoints."""

from pathlib import Path

from fastapi.testclient import TestClient

from {{ cookiecutter.package_name }}.api.main import app

client = TestClient(app)


def test_health_endpoint() -> None:
    """Tests the /health endpoint for a 200 status."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_api_version() -> None:
    """Tests the /version endpoint to reach 100% coverage."""
    response = client.get("/version")
    assert response.status_code == 200

    # Dynamic file reading for comparison from project root
    expected_version = (Path(__file__).resolve().parents[2] / "VERSION").read_text().strip()
    assert response.json() == {"version": expected_version}


def test_api_home() -> None:
    """Tests the root API route."""
    response = client.get("/base/")
    assert response.status_code == 200
    assert "Welcome to my API!" in response.json()["message"]


def test_api_hello() -> None:
    """Tests the /hello route defined in greetings.py."""
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world!"}


def test_api_bonjour() -> None:
    """Tests the /bonjour route defined in greetings.py."""
    response = client.get("/bonjour")
    assert response.status_code == 200
    assert response.json() == {"message": "Bonjour le monde !"}


def test_app_metadata() -> None:
    """Verify that FastAPI initialization parameters are correct."""
    assert app.title == "{{ cookiecutter.package_name }}"
    assert app.description == "API for {{ cookiecutter.package_name }} package"
    # Verify that get_project_version() was called correctly
    expected_version = (Path(__file__).resolve().parents[2] / "VERSION").read_text().strip()
    assert app.version == expected_version
