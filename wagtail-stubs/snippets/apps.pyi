from django.apps import AppConfig
from typing import Any

class WagtailSnippetsAppConfig(AppConfig):
    name: str = ...
    label: str = ...
    verbose_name: Any = ...
