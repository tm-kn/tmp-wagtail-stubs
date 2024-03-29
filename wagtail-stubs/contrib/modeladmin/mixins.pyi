from typing import Any

class ThumbnailMixin:
    thumb_image_field_name: str = ...
    thumb_image_filter_spec: str = ...
    thumb_image_width: int = ...
    thumb_classname: str = ...
    thumb_col_header_text: Any = ...
    thumb_default: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def admin_thumb(self, obj: Any): ...
