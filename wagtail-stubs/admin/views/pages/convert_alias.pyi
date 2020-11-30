from typing import Any
from wagtail.admin import messages as messages
from wagtail.admin.views.pages.utils import get_valid_next_url_from_request as get_valid_next_url_from_request
from wagtail.core import hooks as hooks
from wagtail.core.models import Page as Page, PageLogEntry as PageLogEntry

def convert_alias(request: Any, page_id: Any): ...
