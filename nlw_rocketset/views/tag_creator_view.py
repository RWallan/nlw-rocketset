from nlw_rocketset.controllers.tag_creator_controller import (
    TagCreateController,
)
from nlw_rocketset.views.http_types.http_request import HttpRequest
from nlw_rocketset.views.http_types.http_response import HttpResponse


class TagCreatorView:
    def __init__(self) -> None:
        self.tag_creator_controller = TagCreateController()

    def validate_and_create(self, http_request: HttpRequest):
        body = http_request.body
        product_code = body["product_code"]

        formatted_response = self.tag_creator_controller.create(product_code)

        return HttpResponse(status_code=200, body=formatted_response)
