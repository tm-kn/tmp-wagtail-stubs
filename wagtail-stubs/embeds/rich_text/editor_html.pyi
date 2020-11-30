from typing import Any
from wagtail.admin.rich_text.converters import editor_html as editor_html
from wagtail.embeds import format as format
from wagtail.embeds.exceptions import EmbedException as EmbedException

class MediaEmbedHandler:
    @staticmethod
    def get_db_attributes(tag: Any): ...
    @staticmethod
    def expand_db_attributes(attrs: Any): ...

EditorHTMLEmbedConversionRule: Any
