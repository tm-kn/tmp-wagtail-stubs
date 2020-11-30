from .registry import registry as registry
from typing import Any
from wagtail.core.models import Site as Site

class SettingsProxy(dict):
    request_or_site: Any = ...
    def __init__(self, request_or_site: Any) -> None: ...
    def __missing__(self, app_label: Any): ...

class SettingModuleProxy(dict):
    app_label: Any = ...
    request_or_site: Any = ...
    def __init__(self, request_or_site: Any, app_label: Any) -> None: ...
    def __getitem__(self, model_name: Any): ...
    def __missing__(self, model_name: Any): ...
    def get_setting(self, model_name: Any): ...

def settings(request: Any): ...
