from .base import Block
from typing import Any, Optional

class ListBlock(Block):
    child_block: Any = ...
    dependencies: Any = ...
    child_js_initializer: Any = ...
    def __init__(self, child_block: Any, **kwargs: Any) -> None: ...
    def get_default(self): ...
    @property
    def media(self): ...
    def render_list_member(self, value: Any, prefix: Any, index: Any, errors: Optional[Any] = ...): ...
    def html_declarations(self): ...
    def js_initializer(self): ...
    def render_form(self, value: Any, prefix: str = ..., errors: Optional[Any] = ...): ...
    def value_from_datadict(self, data: Any, files: Any, prefix: Any): ...
    def value_omitted_from_data(self, data: Any, files: Any, prefix: Any): ...
    def clean(self, value: Any): ...
    def to_python(self, value: Any): ...
    def bulk_to_python(self, values: Any): ...
    def get_prep_value(self, value: Any): ...
    def get_api_representation(self, value: Any, context: Optional[Any] = ...): ...
    def render_basic(self, value: Any, context: Optional[Any] = ...): ...
    def get_searchable_content(self, value: Any): ...
    def check(self, **kwargs: Any): ...
    class Meta:
        icon: str = ...
