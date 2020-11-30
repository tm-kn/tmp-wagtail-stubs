from typing import Any
from wagtail.admin import messages as messages
from wagtail.admin.auth import user_has_any_page_permission as user_has_any_page_permission, user_passes_test as user_passes_test
from wagtail.admin.forms.pages import CopyForm as CopyForm
from wagtail.admin.views.pages.utils import get_valid_next_url_from_request as get_valid_next_url_from_request
from wagtail.core import hooks as hooks
from wagtail.core.models import Page as Page

def copy(request: Any, page_id: Any): ...
