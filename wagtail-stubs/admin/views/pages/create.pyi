from django.views.generic.base import ContextMixin, TemplateResponseMixin, View
from typing import Any
from wagtail.admin import messages as messages, signals as signals
from wagtail.admin.action_menu import PageActionMenu as PageActionMenu
from wagtail.admin.views.generic import HookResponseMixin as HookResponseMixin
from wagtail.admin.views.pages.utils import get_valid_next_url_from_request as get_valid_next_url_from_request
from wagtail.core.models import Locale as Locale, Page as Page, UserPagePermissionsProxy as UserPagePermissionsProxy

def add_subpage(request: Any, parent_page_id: Any): ...

class CreateView(TemplateResponseMixin, ContextMixin, HookResponseMixin, View):
    template_name: str = ...
    parent_page: Any = ...
    parent_page_perms: Any = ...
    page_content_type: Any = ...
    page_class: Any = ...
    locale: Any = ...
    page: Any = ...
    edit_handler: Any = ...
    form_class: Any = ...
    next_url: Any = ...
    def dispatch(self, request: Any, content_type_app_name: Any, content_type_model_name: Any, parent_page_id: Any): ...
    form: Any = ...
    def post(self, request: Any): ...
    def form_valid(self, form: Any): ...
    def get_edit_message_button(self): ...
    def get_view_draft_message_button(self): ...
    def get_view_live_message_button(self): ...
    def save_action(self): ...
    def publish_action(self): ...
    def submit_action(self): ...
    def redirect_away(self): ...
    def redirect_and_remain(self): ...
    has_unsaved_changes: bool = ...
    def form_invalid(self, form: Any): ...
    def get(self, request: Any): ...
    def get_context_data(self, **kwargs: Any): ...
