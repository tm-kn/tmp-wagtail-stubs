from typing import Any
from wagtail.admin.rich_text.converters import editor_html as editor_html
from wagtail.images import get_image_model as get_image_model
from wagtail.images.formats import get_image_format as get_image_format

class ImageEmbedHandler:
    @staticmethod
    def get_db_attributes(tag: Any): ...
    @staticmethod
    def expand_db_attributes(attrs: Any): ...

EditorHTMLImageConversionRule: Any
