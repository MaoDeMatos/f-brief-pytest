from flask import Flask
import pytest


@pytest.mark.content
@pytest.mark.expectSuccess
def test_content_homepage(client: Flask):
    response = client.test_client().get("/")
    assert b"Hello, World" in response.data


# As the successful and failing tests have the same code,
# I exported it here
def http_test_to_other(client: Flask, arg):
    arg = str(arg)
    response = client.test_client().get("/other?page=" + arg)
    expected = "Page : " + arg
    return expected.encode() in response.data


@pytest.mark.content
@pytest.mark.expectSuccess
@pytest.mark.parametrize("page_num", [22, 747])
def test_content_other_page(client: Flask, page_num: int):
    assert http_test_to_other(client, page_num)


# @pytest.mark.skip(reason="Not fully implemented yet")
@pytest.mark.content
@pytest.mark.expectFail
@pytest.mark.parametrize("page_num", [654.99654, "string"])
def test_content_other_page_bad_arg_type(client: Flask, page_num: int):
    assert not http_test_to_other(client, page_num)
