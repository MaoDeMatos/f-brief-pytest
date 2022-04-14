import json
from flask import Flask
import pytest
from app import app


# Returns the app Flask object
@pytest.fixture(scope="session")
def client():
    app.config.update({"TESTING": True})
    yield app.test_client()


@pytest.fixture
def mock_cats():
    cats = {
        "catsList": [
            {"id": 1, "name": "Tqsdkaze"},
            {"id": 2, "name": "Dlqspoeaz"},
            {"id": 3, "name": "Pqsdmlaze"},
            {"id": 4, "name": "QSDljfsq"},
        ]
    }
    return json.dumps(cats)


@pytest.fixture
def flask_response(client: Flask.test_client):
    def _func(url):
        return client.get(url)
    return _func
