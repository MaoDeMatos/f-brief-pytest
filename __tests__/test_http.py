from flask import Flask
import pytest
import os

# app_url = os.environ["APP_URL"] + ":" + os.environ["APP_PORT"]

# test_app = Flask(__name__)


@pytest.mark.get_request
def test_flask_is_started(client: Flask):
    response = client.test_client().get("/")
    assert response.status_code == 200
