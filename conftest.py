import json
import pytest
from app import app

# Returns the app Flask object
@pytest.fixture
def client():
    return app.test_client()

@pytest.fixture
def mock_cats():
    cats = { "catsList": [{ "id": 1, "name":"Tqsdkaze" }, { "id": 2, "name":"Dlqspoeaz" }] }
    return json.load(cats)