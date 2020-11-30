from django.utils.deprecation import MiddlewareMixin
from typing import Any
from wagtail.contrib.redirects import models as models
from wagtail.core.models import Site as Site

def get_redirect(request: Any, path: Any): ...

class RedirectMiddleware(MiddlewareMixin):
    def process_response(self, request: Any, response: Any): ...
