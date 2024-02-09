from flask import Blueprint, jsonify, request

from nlw_rocketset.errors.error_handler import handle_errors
from nlw_rocketset.validators.tag_creator_validator import (
    tag_creator_validator,
)
from nlw_rocketset.views.http_types.http_request import HttpRequest
from nlw_rocketset.views.tag_creator_view import TagCreatorView

tags_routes_bp = Blueprint("tags_routes", __name__)


@tags_routes_bp.route("/create_tag", methods=["POST"])
def create_tags():
    try:
        tag_creator_validator(request)
        tag_creator_view = TagCreatorView()
        print(request.json)

        http_request = HttpRequest(body=request.json)
        response = tag_creator_view.validate_and_create(http_request)
    except Exception as error:
        response = handle_errors(error)

    return jsonify(response.body), response.status_code
