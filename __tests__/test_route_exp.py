import pytest


# pytest.skip(allow_module_level=True)


@pytest.mark.htmlContent
@pytest.mark.expectSuccess
@pytest.mark.parametrize("value", [22, 747, -9])
def test_get_exp_page(route_response_getter, value: int):
    value = str(value)
    response = route_response_getter("/exp?value=" + value)
    expected = "Exposant 2 de " + value
    # + str(pow(value, 2))
    assert expected.encode() in response.data


@pytest.mark.htmlContent
@pytest.mark.expectFail
def test_get_exp_page_no_value(route_response_getter):
    with pytest.raises(TypeError):
        route_response_getter("/exp")


@pytest.mark.htmlContent
@pytest.mark.expectFail
@pytest.mark.parametrize("value", [654.99654, "string", False])
def test_get_exp_page_bad_value_type(route_response_getter, value: int):
    with pytest.raises(ValueError):
        route_response_getter("/exp?value=" + str(value))
