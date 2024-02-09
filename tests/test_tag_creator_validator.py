import pytest

from nlw_rocketset.error_types.http_unprocessable_entity import (
    HttpUnprocessableEntityError,
)
from nlw_rocketset.validators.tag_creator_validator import (
    tag_creator_validator,
)


class MockRequest:
    def __init__(self, json: dict) -> None:
        self.json = json


def test_tag_creator_validator():
    req = MockRequest(json={"product_code": "12345"})

    response = tag_creator_validator(req)

    assert not response


def test_tag_creator_validator_with_error():

    req = MockRequest(json={"product_code": 12345})

    with pytest.raises(HttpUnprocessableEntityError):
        tag_creator_validator(req)
