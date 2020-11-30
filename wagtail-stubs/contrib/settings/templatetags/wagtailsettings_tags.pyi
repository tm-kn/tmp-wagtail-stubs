from ..context_processors import SettingsProxy as SettingsProxy
from typing import Any
from wagtail.core.models import Site as Site

register: Any

def get_settings(context: Any, use_default_site: bool = ...): ...
