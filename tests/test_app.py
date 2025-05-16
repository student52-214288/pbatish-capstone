import os
import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


@pytest.fixture
def set_env_vars():
    os.environ["APP_NAME"] = "Test App"
    os.environ["AUTHOR_NAME"] = "Pbatish"
    os.environ["ENVIRONMENT"] = "test"
    os.environ["SECRET_KEY"] = "test-secret-key"
    yield
    del os.environ["APP_NAME"]
    del os.environ["ENVIRONMENT"]
    del os.environ["SECRET_KEY"]
    del os.environ['AUTHOR_NAME']


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "OK",
        "message": "The application is healthy!"}


def test_get_version():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}


def test_get_env(set_env_vars):
    response = client.get("/env")
    assert response.status_code == 200
    assert response.json() == {
        "app_name": "Test App",
        "environment": "test",
        "secret_key": "test-secret-key",
        "author_name": "Pbatish"
    }

