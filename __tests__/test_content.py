import json
import pytest
from flask import Flask
from pytest_mock import mocker


@pytest.mark.htmlContent
@pytest.mark.expectSuccess
def test_get_homepage(client: Flask.test_client):
    response = client.get("/")
    assert b"Hello, World" in response.data


# As the successful and failing tests have the same code,
# I exported it here
def http_test_to_other(client: Flask.test_client, arg):
    arg = str(arg)
    response = client.get("/other?page=" + arg)
    expected = "Page : " + arg
    return expected.encode() in response.data


@pytest.mark.htmlContent
@pytest.mark.expectSuccess
@pytest.mark.parametrize("page_num", [22, 747])
def test_get_other_page(client: Flask.test_client, page_num: int):
    assert http_test_to_other(client, page_num)


@pytest.mark.htmlContent
@pytest.mark.expectFail
@pytest.mark.parametrize("page_num", [654.99654, "string"])
def test_get_other_page_bad_arg_type(client: Flask.test_client, page_num: int):
    assert not http_test_to_other(client, page_num)


@pytest.mark.jsonContent
@pytest.mark.expectSuccess
def test_get_cats_endpoint(client: Flask.test_client):
    res = client.get('/cats')
    json_data = json.loads(res.get_data(as_text=True))
    assert res.status_code == 200
    assert "catsList" in json_data


@pytest.mark.skip(reason="Not fully implemented yet")
@pytest.mark.jsonContent
@pytest.mark.expectSuccess
@pytest.mark.mockData
def test_get_cats_endpoint_mock(mock_cats, mocker: mocker):
    def get_mock_data():
        return mock_cats

    mocker.patch("/cats", get_mock_data)

    assert True
