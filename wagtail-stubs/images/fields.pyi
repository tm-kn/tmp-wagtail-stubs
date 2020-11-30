from django.forms.fields import ImageField
from typing import Any

ALLOWED_EXTENSIONS: Any
SUPPORTED_FORMATS_TEXT: Any

class WagtailImageField(ImageField):
    max_upload_size: Any = ...
    max_image_pixels: Any = ...
    help_text: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def check_image_file_format(self, f: Any) -> None: ...
    def check_image_file_size(self, f: Any) -> None: ...
    def check_image_pixel_size(self, f: Any) -> None: ...
    def to_python(self, data: Any): ...