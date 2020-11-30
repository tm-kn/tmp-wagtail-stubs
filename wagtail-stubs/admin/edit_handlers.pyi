from .forms.models import DIRECT_FORM_FIELD_OVERRIDES as DIRECT_FORM_FIELD_OVERRIDES, FORM_FIELD_OVERRIDES as FORM_FIELD_OVERRIDES, WagtailAdminModelForm as WagtailAdminModelForm, formfield_for_dbfield as formfield_for_dbfield
from .forms.pages import WagtailAdminPageForm as WagtailAdminPageForm
from typing import Any, Optional
from wagtail.admin import compare as compare, widgets as widgets
from wagtail.core.fields import RichTextField as RichTextField
from wagtail.core.models import Page as Page
from wagtail.core.utils import camelcase_to_underscore as camelcase_to_underscore, resolve_model_string as resolve_model_string
from wagtail.utils.decorators import cached_classmethod as cached_classmethod

def widget_with_script(widget: Any, script: Any): ...
def get_form_for_model(model: Any, form_class: Any = ..., fields: Optional[Any] = ..., exclude: Optional[Any] = ..., formsets: Optional[Any] = ..., exclude_formsets: Optional[Any] = ..., widgets: Optional[Any] = ...): ...
def extract_panel_definitions_from_model_class(model: Any, exclude: Optional[Any] = ...): ...

class EditHandler:
    heading: Any = ...
    classname: Any = ...
    help_text: Any = ...
    model: Any = ...
    instance: Any = ...
    request: Any = ...
    form: Any = ...
    def __init__(self, heading: str = ..., classname: str = ..., help_text: str = ...) -> None: ...
    def clone(self): ...
    def clone_kwargs(self): ...
    def widget_overrides(self): ...
    def required_fields(self): ...
    def required_formsets(self): ...
    def html_declarations(self): ...
    def bind_to(self, model: Optional[Any] = ..., instance: Optional[Any] = ..., request: Optional[Any] = ..., form: Optional[Any] = ...): ...
    def on_model_bound(self) -> None: ...
    def on_instance_bound(self) -> None: ...
    def on_request_bound(self) -> None: ...
    def on_form_bound(self) -> None: ...
    def classes(self): ...
    def field_type(self): ...
    def id_for_label(self): ...
    def render_as_object(self): ...
    def render_as_field(self): ...
    def render_missing_fields(self): ...
    def render_form_content(self): ...
    def get_comparison(self): ...

class BaseCompositeEditHandler(EditHandler):
    children: Any = ...
    def __init__(self, children: Any = ..., *args: Any, **kwargs: Any) -> None: ...
    def clone_kwargs(self): ...
    def widget_overrides(self): ...
    def required_fields(self): ...
    def required_formsets(self): ...
    def html_declarations(self): ...
    def on_model_bound(self) -> None: ...
    def on_instance_bound(self) -> None: ...
    def on_request_bound(self) -> None: ...
    def on_form_bound(self) -> None: ...
    def render(self): ...
    def get_comparison(self): ...

class BaseFormEditHandler(BaseCompositeEditHandler):
    base_form_class: Any = ...
    def get_form_class(self): ...

class TabbedInterface(BaseFormEditHandler):
    template: str = ...
    base_form_class: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def clone_kwargs(self): ...

class ObjectList(TabbedInterface):
    template: str = ...

class FieldRowPanel(BaseCompositeEditHandler):
    template: str = ...
    def on_instance_bound(self) -> None: ...

class MultiFieldPanel(BaseCompositeEditHandler):
    template: str = ...
    def classes(self): ...

class HelpPanel(EditHandler):
    content: Any = ...
    template: Any = ...
    def __init__(self, content: str = ..., template: str = ..., heading: str = ..., classname: str = ...) -> None: ...
    def clone_kwargs(self): ...
    def render(self): ...

class FieldPanel(EditHandler):
    TEMPLATE_VAR: str = ...
    widget: Any = ...
    field_name: Any = ...
    def __init__(self, field_name: Any, *args: Any, **kwargs: Any) -> None: ...
    def clone_kwargs(self): ...
    def widget_overrides(self): ...
    def classes(self): ...
    def field_type(self): ...
    def id_for_label(self): ...
    object_template: str = ...
    def render_as_object(self): ...
    field_template: str = ...
    def render_as_field(self): ...
    def required_fields(self): ...
    def get_comparison_class(self): ...
    def get_comparison(self): ...
    def db_field(self): ...
    bound_field: Any = ...
    heading: Any = ...
    help_text: Any = ...
    def on_form_bound(self) -> None: ...

class RichTextFieldPanel(FieldPanel):
    def get_comparison_class(self): ...

class BaseChooserPanel(FieldPanel):
    def get_chosen_item(self): ...
    def render_as_field(self): ...

class PageChooserPanel(BaseChooserPanel):
    object_type_name: str = ...
    page_type: Any = ...
    can_choose_root: Any = ...
    def __init__(self, field_name: Any, page_type: Optional[Any] = ..., can_choose_root: bool = ...) -> None: ...
    def clone_kwargs(self): ...
    def widget_overrides(self): ...
    def target_models(self): ...

class InlinePanel(EditHandler):
    relation_name: Any = ...
    panels: Any = ...
    heading: Any = ...
    label: Any = ...
    min_num: Any = ...
    max_num: Any = ...
    def __init__(self, relation_name: Any, panels: Optional[Any] = ..., heading: str = ..., label: str = ..., min_num: Optional[Any] = ..., max_num: Optional[Any] = ..., *args: Any, **kwargs: Any) -> None: ...
    def clone_kwargs(self): ...
    def get_panel_definitions(self): ...
    def get_child_edit_handler(self): ...
    def required_formsets(self): ...
    def html_declarations(self): ...
    def get_comparison(self): ...
    db_field: Any = ...
    def on_model_bound(self) -> None: ...
    formset: Any = ...
    children: Any = ...
    empty_child: Any = ...
    def on_form_bound(self): ...
    template: str = ...
    def render(self): ...
    js_template: str = ...
    def render_js_init(self): ...

class PublishingPanel(MultiFieldPanel):
    def __init__(self, **kwargs: Any) -> None: ...

class PrivacyModalPanel(EditHandler):
    def __init__(self, **kwargs: Any) -> None: ...
    def render(self): ...

def get_edit_handler(cls): ...

class StreamFieldPanel(FieldPanel):
    def classes(self): ...
    def html_declarations(self): ...
    def get_comparison_class(self): ...
    def id_for_label(self): ...
    block_def: Any = ...
    def on_model_bound(self) -> None: ...
