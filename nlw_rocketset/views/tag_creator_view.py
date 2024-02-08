from nlw_rocketset.views.http_types.http_request import HttpRequest
from nlw_rocketset.views.http_types.http_response import HttpResponse


class TagCreatorView:
    def validate_and_create(self, http_request: HttpRequest):

        return HttpResponse(status_code=200, body={"hello": "world"})
