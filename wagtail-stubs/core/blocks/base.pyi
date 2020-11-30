from django import forms
from typing import Any, Optional

class BaseBlock(type):
    def __new__(mcs: Any, name: Any, bases: Any, attrs: Any): ...

class Block(metaclass=BaseBlock):
    name: str = ...
    creation_counter: int = ...
    TEMPLATE_VAR: str = ...
    class Meta:
        label: Any = ...
        icon: str = ...
        classname: Any = ...
        group: str = ...
    dependencies: Any = ...
    def __new__(cls, *args: Any, **kwargs: Any): ...
    def all_blocks(self): ...
    def all_media(self): ...
    def all_html_declarations(self): ...
    meta: Any = ...
    definition_prefix: Any = ...
    label: Any = ...
    def __init__(self, **kwargs: Any) -> None: ...
    def set_name(self, name: Any) -> None: ...
    @property
    def media(self): ...
    def html_declarations(self): ...
    def js_initializer(self) -> None: ...
    def render_form(self, value: Any, prefix: str = ..., errors: Optional[Any] = ...) -> None: ...
    def value_from_datadict(self, data: Any, files: Any, prefix: Any) -> None: ...
    def value_omitted_from_data(self, data: Any, files: Any, name: Any): ...
    def bind(self, value: Any, prefix: Optional[Any] = ..., errors: Optional[Any] = ...): ...
    def get_default(self): ...
    def prototype_block(self): ...
    def clean(self, value: Any): ...
    def to_python(self, value: Any): ...
    def bulk_to_python(self, values: Any): ...
    def get_prep_value(self, value: Any): ...
    def get_context(self, value: Any, parent_context: Optional[Any] = ...): ...
    def get_template(self, context: Optional[Any] = ...): ...
    def render(self, value: Any, context: Optional[Any] = ...): ...
    def get_api_representation(self, value: Any, context: Optional[Any] = ...): ...
    def render_basic(self, value: Any, context: Optional[Any] = ...): ...
    def get_searchable_content(self, value: Any): ...
    def check(self, **kwargs: Any): ...
    def id_for_label(self, prefix: Any) -> None: ...
    @property
    def required(self): ...
    def deconstruct(self): ...
    def __eq__(self, other: Any) -> Any: ...

class BoundBlock:
    block: Any = ...
    value: Any = ...
    prefix: Any = ...
    errors: Any = ...
    def __init__(self, block: Any, value: Any, prefix: Optional[Any] = ..., errors: Optional[Any] = ...) -> None: ...
    def render_form(self): ...
    def render(self, context: Optional[Any] = ...): ...
    def render_as_block(self, context: Optional[Any] = ...): ...
    def id_for_label(self): ...

class DeclarativeSubBlocksMetaclass(BaseBlock):
    def __new__(mcs: Any, name: Any, bases: Any, attrs: Any): ...

class BlockWidget(forms.Widget):
    block_def: Any = ...
    def __init__(self, block_def: Any, attrs: Optional[Any] = ...) -> None: ...
    def render_with_errors(self, name: Any, value: Any, attrs: Optional[Any] = ..., errors: Optional[Any] = ..., renderer: Optional[Any] = ...): ...
    def render(self, name: Any, value: Any, attrs: Optional[Any] = ..., renderer: Optional[Any] = ...): ...
    @property
    def media(self): ...
    def value_from_datadict(self, data: Any, files: Any, name: Any): ...
    def value_omitted_from_data(self, data: Any, files: Any, name: Any): ...

class BlockField(forms.Field):
    block: Any = ...
    def __init__(self, block: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def clean(self, value: Any): ...
    def has_changed(self, initial_value: Any, data_value: Any): ...
