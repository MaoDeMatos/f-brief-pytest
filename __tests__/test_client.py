from flask import Flask
import pytest


@pytest.mark.getRequest
@pytest.mark.expectSuccess
@pytest.mark.parametrize("route", ["/", "/other"])
def test_route_exists(client: Flask, route: str):
    response = client.test_client().get(route)
    assert response.status_code == 200
    assert "Hello".encode() in response.data


@pytest.mark.getRequest
@pytest.mark.expectFail
@pytest.mark.parametrize("route", [654, "/do-not-exist"])
def test_route_do_not_exists(client: Flask, route):
    response = client.test_client().get(str(route))
    assert response.status_code == 404
    assert not "Hello".encode() in response.data
