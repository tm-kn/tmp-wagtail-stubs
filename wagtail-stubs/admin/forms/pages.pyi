from .models import WagtailAdminModelForm as WagtailAdminModelForm
from .view_restrictions import BaseViewRestrictionForm as BaseViewRestrictionForm
from django import forms
from typing import Any, Optional
from wagtail.admin import widgets as widgets
from wagtail.core.models import Page as Page, PageViewRestriction as PageViewRestriction

class CopyForm(forms.Form):
    page: Any = ...
    user: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def clean(self): ...

class PageViewRestrictionForm(BaseViewRestrictionForm): ...

class WagtailAdminPageForm(WagtailAdminModelForm):
    parent_page: Any = ...
    def __init__(self, data: Optional[Any] = ..., files: Optional[Any] = ..., parent_page: Optional[Any] = ..., *args: Any, **kwargs: Any) -> None: ...
    def clean(self): ...
