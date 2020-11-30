from .shortcuts import get_rendition_or_not_found as get_rendition_or_not_found
from .templatetags.wagtailimages_tags import image_url as image_url
from jinja2.ext import Extension
from typing import Any

allowed_filter_pattern: Any

def image(image: Any, filterspec: Any, **attrs: Any): ...

class WagtailImagesExtension(Extension):
    def __init__(self, environment: Any) -> None: ...
images = WagtailImagesExtension
