from nlw_rocketset.views.http_types.http_response import HttpResponse


def handle_errors(error: Exception) -> HttpResponse:
    return HttpResponse(
        status_code=500,
        body={"error": [{"title": "Server Error", "detail": str(error)}]},
    )
