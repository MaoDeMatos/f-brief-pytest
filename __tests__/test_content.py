import json
import pytest
from flask import Flask
from pytest_mock import mocker


def get_route_response(client: Flask.test_client, url: str):
    return client.get(url)


# /


@pytest.mark.htmlContent
@pytest.mark.expectSuccess
def test_get_homepage(client: Flask.test_client):
    response = get_route_response(client, "/")
    assert b"Hello, World" in response.data


# /other


# As the successful and failing tests have the same code,
# I exported it here
def http_test_to_other(client: Flask.test_client, arg):
    arg = str(arg)
    response = get_route_response(client, "/other?page=" + arg)
    expected = "Page : " + arg
    return expected.encode() in response.data


@pytest.mark.htmlContent
@pytest.mark.expectSuccess
@pytest.mark.parametrize("page_num", [22, 747, -9])
def test_get_other_page(client: Flask.test_client, page_num: int):
    assert http_test_to_other(client, page_num)


@pytest.mark.htmlContent
@pytest.mark.expectFail
@pytest.mark.parametrize("page_num", [654.99654, "string"])
def test_get_other_page_bad_arg_type(client: Flask.test_client, page_num: int):
    assert not http_test_to_other(client, page_num)


# /exp


def http_test_to_exp(client: Flask.test_client, arg):
    arg = str(arg)
    response = get_route_response(client, "/exp?value=" + arg)
    expected = "Exposant 2 de " + arg
    # + str(pow(arg, 2))
    return expected.encode() in response.data


@pytest.mark.htmlContent
@pytest.mark.expectSuccess
@pytest.mark.parametrize("value", [22, 747, -9])
def test_get_exp_page(client: Flask.test_client, value: int):
    assert http_test_to_exp(client, value)


@pytest.mark.htmlContent
@pytest.mark.expectFail
@pytest.mark.parametrize("value", [654.99654, "string"])
def test_get_exp_page_bad_arg_type(client: Flask.test_client, value: int):
    assert not http_test_to_exp(client, value)


# /cats


@pytest.mark.jsonContent
@pytest.mark.expectSuccess
def test_get_cats_endpoint(client: Flask.test_client):
    res = get_route_response(client, "/cats")
    json_data = json.loads(res.get_data(as_text=True))
    assert res.status_code == 200
    assert json_data.get("catsList")


# @pytest.mark.skip(reason="Not fully implemented yet")
@pytest.mark.jsonContent
@pytest.mark.expectSuccess
@pytest.mark.mockData
def test_get_cats_endpoint_mock(client: Flask, mock_cats: str, mocker: mocker):
    mocker.patch("test_content.get_route_response", return_value=mock_cats)
    assert mock_cats == get_route_response(client, "/cats")
