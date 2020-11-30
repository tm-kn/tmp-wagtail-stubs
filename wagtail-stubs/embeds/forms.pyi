from django import forms
from typing import Any

class EmbedForm(forms.Form):
    url: Any = ...
