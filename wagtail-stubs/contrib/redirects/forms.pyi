from django import forms
from typing import Any
from wagtail.admin.widgets import AdminPageChooser as AdminPageChooser
from wagtail.contrib.redirects.models import Redirect as Redirect
from wagtail.core.models import Site as Site

class RedirectForm(forms.ModelForm):
    site: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    required_css_class: str = ...
    def clean(self) -> None: ...

class ImportForm(forms.Form):
    import_file: Any = ...
    def __init__(self, allowed_extensions: Any, *args: Any, **kwargs: Any) -> None: ...

class ConfirmImportForm(forms.Form):
    from_index: Any = ...
    to_index: Any = ...
    site: Any = ...
    permanent: Any = ...
    import_file_name: Any = ...
    original_file_name: Any = ...
    input_format: Any = ...
    def __init__(self, headers: Any, *args: Any, **kwargs: Any) -> None: ...
    def clean_import_file_name(self): ...
