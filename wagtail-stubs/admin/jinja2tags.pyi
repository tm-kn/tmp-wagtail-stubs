from .templatetags.wagtailuserbar import wagtailuserbar as wagtailuserbar
from jinja2.ext import Extension
from typing import Any

class WagtailUserbarExtension(Extension):
    def __init__(self, environment: Any) -> None: ...
userbar = WagtailUserbarExtension
