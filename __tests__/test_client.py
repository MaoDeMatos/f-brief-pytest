from flask import Flask
import pytest


@pytest.mark.get_request
def test_flask_exists(client: Flask):
    response = client.test_client().get("/")
    assert response.status_code == 200
