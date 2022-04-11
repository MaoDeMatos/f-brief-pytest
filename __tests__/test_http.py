import pytest
import os

from app import app

# app_url = os.environ["APP_URL"] + ":" + os.environ["APP_PORT"]

# test_app = Flask(__name__)


@pytest.mark.get_request
def test_flask_is_started():
    response = app.test_client().get("/")
    assert response.status_code == 200
