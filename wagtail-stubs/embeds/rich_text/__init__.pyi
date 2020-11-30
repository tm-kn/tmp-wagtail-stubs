from typing import Any
from wagtail.core.rich_text import EmbedHandler as EmbedHandler
from wagtail.embeds import format as format
from wagtail.embeds.embeds import get_embed as get_embed
from wagtail.embeds.models import Embed as Embed

class MediaEmbedHandler(EmbedHandler):
    identifier: str = ...
    @staticmethod
    def get_model(): ...
    @staticmethod
    def get_instance(attrs: Any): ...
    @staticmethod
    def expand_db_attributes(attrs: Any): ...
