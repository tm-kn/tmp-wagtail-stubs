from django.forms import widgets
from typing import Any, Optional
from wagtail.admin.datetimepicker import to_datetimepicker_format as to_datetimepicker_format
from wagtail.admin.staticfiles import versioned_static as versioned_static

DEFAULT_DATE_FORMAT: str
DEFAULT_DATETIME_FORMAT: str
DEFAULT_TIME_FORMAT: str

class AdminDateInput(widgets.DateInput):
    template_name: str = ...
    js_format: Any = ...
    def __init__(self, attrs: Optional[Any] = ..., format: Optional[Any] = ...) -> None: ...
    def get_context(self, name: Any, value: Any, attrs: Any): ...
    @property
    def media(self): ...

class AdminTimeInput(widgets.TimeInput):
    template_name: str = ...
    js_format: Any = ...
    def __init__(self, attrs: Optional[Any] = ..., format: Optional[Any] = ...) -> None: ...
    def get_context(self, name: Any, value: Any, attrs: Any): ...
    @property
    def media(self): ...

class AdminDateTimeInput(widgets.DateTimeInput):
    template_name: str = ...
    js_format: Any = ...
    js_time_format: Any = ...
    def __init__(self, attrs: Optional[Any] = ..., format: Optional[Any] = ..., time_format: Optional[Any] = ...) -> None: ...
    def get_context(self, name: Any, value: Any, attrs: Any): ...
    @property
    def media(self): ...