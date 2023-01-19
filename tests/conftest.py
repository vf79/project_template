import pytest
from fastapi.testclient import TestClient

from app.config import config
from app.main import create_app


@pytest.fixture(scope="module")
def client():
    app = create_app()
    return TestClient(app)


@pytest.fixture(scope="module")
def settings():
    settings = config.get_settings()
    return settings
