import requests
import os

app_url = os.environ["APP_URL"] + ":" + os.environ["APP_PORT"]


def test_flask_is_started():
    response = requests.get(app_url)
    assert response.status_code == 200
