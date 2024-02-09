from typing import Any

from cerberus import Validator

from nlw_rocketset.error_types.http_unprocessable_entity import (
    HttpUnprocessableEntityError,
)


def tag_creator_validator(request: Any):
    body_validator = Validator(
        {"product_code": {"type": "string", "required": True, "empty": False}}
    )

    response = body_validator.validate(request.json)

    if not response:
        raise HttpUnprocessableEntityError(body_validator.errors)