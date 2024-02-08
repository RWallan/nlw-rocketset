from typing import Optional


class HttpRequest:
    def __init__(
        self,
        header: Optional[dict] = None,
        body: Optional[dict] = None,
        query_params: Optional[dict] = None,
    ) -> None:
        self.header = header
        self.body = body
        self.query_params = query_params
