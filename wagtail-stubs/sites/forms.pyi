from django import forms
from typing import Any
from wagtail.admin.widgets import AdminPageChooser as AdminPageChooser
from wagtail.core.models import Site as Site

class SiteForm(forms.ModelForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    required_css_class: str = ...
