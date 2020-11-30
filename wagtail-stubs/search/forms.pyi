from django import forms
from typing import Any

class QueryForm(forms.Form):
    query_string: Any = ...
