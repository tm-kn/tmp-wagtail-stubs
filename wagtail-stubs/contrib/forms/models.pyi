from .forms import FormBuilder as FormBuilder, WagtailAdminFormPageForm as WagtailAdminFormPageForm
from django.db import models
from typing import Any, Optional
from wagtail.admin.edit_handlers import FieldPanel as FieldPanel
from wagtail.admin.mail import send_mail as send_mail
from wagtail.contrib.forms.utils import get_field_clean_name as get_field_clean_name
from wagtail.core.models import Orderable as Orderable, Page as Page

FORM_FIELD_CHOICES: Any

class AbstractFormSubmission(models.Model):
    form_data: Any = ...
    page: Any = ...
    submit_time: Any = ...
    def get_data(self): ...

class FormSubmission(AbstractFormSubmission): ...

class AbstractFormField(Orderable):
    clean_name: Any = ...
    label: Any = ...
    field_type: Any = ...
    required: Any = ...
    choices: Any = ...
    default_value: Any = ...
    help_text: Any = ...
    panels: Any = ...
    def save(self, *args: Any, **kwargs: Any) -> None: ...
    @classmethod
    def check(cls, **kwargs: Any): ...

class AbstractForm(Page):
    base_form_class: Any = ...
    form_builder: Any = ...
    submissions_list_view_class: Any = ...
    landing_page_template: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def get_form_fields(self): ...
    def get_data_fields(self): ...
    def get_form_class(self): ...
    def get_form_parameters(self): ...
    def get_form(self, *args: Any, **kwargs: Any): ...
    def get_landing_page_template(self, request: Any, *args: Any, **kwargs: Any): ...
    def get_submission_class(self): ...
    def get_submissions_list_view_class(self): ...
    def process_form_submission(self, form: Any): ...
    def render_landing_page(self, request: Any, form_submission: Optional[Any] = ..., *args: Any, **kwargs: Any): ...
    def serve_submissions_list_view(self, request: Any, *args: Any, **kwargs: Any): ...
    def serve(self, request: Any, *args: Any, **kwargs: Any): ...
    preview_modes: Any = ...
    def serve_preview(self, request: Any, mode_name: Any): ...

class AbstractEmailForm(AbstractForm):
    to_address: Any = ...
    from_address: Any = ...
    subject: Any = ...
    def process_form_submission(self, form: Any): ...
    def send_mail(self, form: Any) -> None: ...
    def render_email(self, form: Any): ...
