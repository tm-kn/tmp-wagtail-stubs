from django import forms
from typing import Any

class PasswordViewRestrictionForm(forms.Form):
    password: Any = ...
    return_url: Any = ...
    restriction: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def clean_password(self): ...

class TaskStateCommentForm(forms.Form):
    comment: Any = ...
