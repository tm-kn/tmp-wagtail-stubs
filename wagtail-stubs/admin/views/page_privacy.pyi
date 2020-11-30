from typing import Any
from wagtail.admin.forms.pages import PageViewRestrictionForm as PageViewRestrictionForm
from wagtail.admin.modal_workflow import render_modal_workflow as render_modal_workflow
from wagtail.core.models import Page as Page, PageViewRestriction as PageViewRestriction

def set_privacy(request: Any, page_id: Any): ...
