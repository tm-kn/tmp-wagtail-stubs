from django.apps import AppConfig
from typing import Any
from wagtail.search.signal_handlers import register_signal_handlers as register_signal_handlers

class WagtailSearchAppConfig(AppConfig):
    name: str = ...
    label: str = ...
    verbose_name: Any = ...
    def ready(self) -> None: ...
