from typing import Any
from wagtail.core import hooks as hooks
from wagtail.core.forms import PasswordViewRestrictionForm as PasswordViewRestrictionForm
from wagtail.core.models import Page as Page, PageViewRestriction as PageViewRestriction, Site as Site

def serve(request: Any, path: Any): ...
def authenticate_with_password(request: Any, page_view_restriction_id: Any, page_id: Any): ...
