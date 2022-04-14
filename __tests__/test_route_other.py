import pytest


# pytest.skip(allow_module_level=True)


# As the successful and failing tests have the same code,
# I exported it here
def http_test_to_other(client, arg):
    arg = str(arg)
    response = client("/other?page=" + arg)
    expected = "Page : " + arg
    return expected.encode() in response.data


@pytest.mark.htmlContent
@pytest.mark.expectSuccess
@pytest.mark.parametrize("page_num", [22, 747, -9])
def test_get_other_page(flask_response, page_num: int):
    page_num = str(page_num)
    r = flask_response("/other?page=" + page_num)
    e = "Page : " + page_num
    assert e.encode() in r.data
    # assert http_test_to_other(flask_response, page_num)


@pytest.mark.htmlContent
@pytest.mark.expectFail
@pytest.mark.parametrize("page_num", [654.99654, "string", True])
def test_get_other_page_bad_arg_type(flask_response, page_num: int):
    page_num = str(page_num)
    r = flask_response("/other?page=" + page_num)
    e = "Page : " + page_num
    assert not e.encode() in r.data
