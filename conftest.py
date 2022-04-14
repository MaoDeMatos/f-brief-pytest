import json
import pytest
from app import app

# Returns the app Flask object
@pytest.fixture
def client():
    return app.test_client()


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
