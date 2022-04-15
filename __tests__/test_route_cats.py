import json
import pytest
from pytest_mock import mocker


@pytest.mark.jsonContent
@pytest.mark.expectSuccess
def test_get_cats_endpoint(flask_response):
    res = flask_response("/cats")
    json_data = json.loads(res.get_data(as_text=True))
    assert res.status_code == 200
    assert json_data.get("catsList")


def get_cats_for_mock_local_function(flask_response):
    return flask_response


@pytest.mark.jsonContent
@pytest.mark.expectSuccess
@pytest.mark.mockData
def test_get_cats_endpoint_mock(mock_cats: str, mocker: mocker):
    mocker.patch(
        __name__ + ".get_cats_for_mock_local_function",
        return_value=mock_cats
    )
    assert mock_cats == get_cats_for_mock_local_function("/cats")
