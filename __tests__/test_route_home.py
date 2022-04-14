import pytest


# pytest.skip(allow_module_level=True)


@pytest.mark.htmlContent
@pytest.mark.expectSuccess
def test_get_homepage(route_response_getter):
    response = route_response_getter("/")
    assert b"Hello, World" in response.data
