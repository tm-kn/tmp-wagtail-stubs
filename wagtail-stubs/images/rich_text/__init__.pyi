from typing import Any
from wagtail.core.rich_text import EmbedHandler as EmbedHandler
from wagtail.images import get_image_model as get_image_model
from wagtail.images.formats import get_image_format as get_image_format

class ImageEmbedHandler(EmbedHandler):
    identifier: str = ...
    @staticmethod
    def get_model(): ...
    @classmethod
    def expand_db_attributes(cls, attrs: Any): ...
