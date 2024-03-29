from django import forms
from typing import Any, Optional
from wagtail.admin.staticfiles import versioned_static as versioned_static
from wagtail.core.blocks import FieldBlock as FieldBlock

DEFAULT_TABLE_OPTIONS: Any

class TableInput(forms.HiddenInput):
    template_name: str = ...
    table_options: Any = ...
    def __init__(self, table_options: Optional[Any] = ..., attrs: Optional[Any] = ...) -> None: ...
    def get_context(self, name: Any, value: Any, attrs: Optional[Any] = ...): ...

class TableBlock(FieldBlock):
    table_options: Any = ...
    field_options: Any = ...
    def __init__(self, required: bool = ..., help_text: Optional[Any] = ..., table_options: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def field(self): ...
    def value_from_form(self, value: Any): ...
    def value_for_form(self, value: Any): ...
    def is_html_renderer(self): ...
    def get_searchable_content(self, value: Any): ...
    def render(self, value: Any, context: Optional[Any] = ...): ...
    @property
    def media(self): ...
    def get_table_options(self, table_options: Optional[Any] = ...): ...
