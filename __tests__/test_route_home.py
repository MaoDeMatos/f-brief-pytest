import pytest


@pytest.mark.htmlContent
@pytest.mark.expectSuccess
def test_get_homepage(flask_response):
    response = flask_response("/")
    assert b"Hello, World" in response.data
