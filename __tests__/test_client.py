import pytest


@pytest.mark.getRequest
@pytest.mark.expectSuccess
@pytest.mark.parametrize("route", ["/", "/other", "/cats"])
def test_route_exists(flask_response, route: str):
    response = flask_response(str(route))
    assert response.status_code == 200


@pytest.mark.getRequest
@pytest.mark.expectFail
@pytest.mark.parametrize("route", [654, "/do-not-exist"])
def test_route_do_not_exists(flask_response, route):
    response = flask_response(str(route))
    assert response.status_code == 404
    assert not "Hello".encode() in response.data
