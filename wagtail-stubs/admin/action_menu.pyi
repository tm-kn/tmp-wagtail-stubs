from django.forms import MediaDefiningClass
from typing import Any, Optional
from wagtail.core import hooks as hooks
from wagtail.core.models import UserPagePermissionsProxy as UserPagePermissionsProxy

class ActionMenuItem(metaclass=MediaDefiningClass):
    order: int = ...
    template: str = ...
    label: str = ...
    name: Any = ...
    classname: str = ...
    icon_name: str = ...
    def __init__(self, order: Optional[Any] = ...) -> None: ...
    def is_shown(self, request: Any, context: Any): ...
    def get_context(self, request: Any, parent_context: Any): ...
    def get_url(self, request: Any, context: Any) -> None: ...
    def render_html(self, request: Any, parent_context: Any): ...

class PublishMenuItem(ActionMenuItem):
    label: Any = ...
    name: str = ...
    template: str = ...
    icon_name: str = ...
    def is_shown(self, request: Any, context: Any): ...
    def get_context(self, request: Any, parent_context: Any): ...

class SubmitForModerationMenuItem(ActionMenuItem):
    label: Any = ...
    name: str = ...
    icon_name: str = ...
    def is_shown(self, request: Any, context: Any): ...
    def get_context(self, request: Any, parent_context: Any): ...

class WorkflowMenuItem(ActionMenuItem):
    template: str = ...
    name: Any = ...
    label: Any = ...
    launch_modal: Any = ...
    icon_name: Any = ...
    def __init__(self, name: Any, label: Any, launch_modal: Any, *args: Any, **kwargs: Any) -> None: ...
    def get_context(self, request: Any, parent_context: Any): ...
    def is_shown(self, request: Any, context: Any): ...

class RestartWorkflowMenuItem(ActionMenuItem):
    label: Any = ...
    name: str = ...
    classname: str = ...
    icon_name: str = ...
    def is_shown(self, request: Any, context: Any): ...

class CancelWorkflowMenuItem(ActionMenuItem):
    label: Any = ...
    name: str = ...
    icon_name: str = ...
    def is_shown(self, request: Any, context: Any): ...

class UnpublishMenuItem(ActionMenuItem):
    label: Any = ...
    name: str = ...
    icon_name: str = ...
    classname: str = ...
    def is_shown(self, request: Any, context: Any): ...
    def get_url(self, request: Any, context: Any): ...

class DeleteMenuItem(ActionMenuItem):
    name: str = ...
    label: Any = ...
    icon_name: str = ...
    classname: str = ...
    def is_shown(self, request: Any, context: Any): ...
    def get_url(self, request: Any, context: Any): ...

class LockMenuItem(ActionMenuItem):
    name: str = ...
    label: Any = ...
    aria_label: Any = ...
    icon_name: str = ...
    classname: str = ...
    template: str = ...
    def is_shown(self, request: Any, context: Any): ...
    def get_url(self, request: Any, context: Any): ...
    def render_html(self, request: Any, parent_context: Any): ...

class UnlockMenuItem(LockMenuItem):
    name: str = ...
    label: Any = ...
    aria_label: Any = ...
    icon_name: str = ...
    def is_shown(self, request: Any, context: Any): ...
    def get_url(self, request: Any, context: Any): ...

class SaveDraftMenuItem(ActionMenuItem):
    name: str = ...
    label: Any = ...
    template: str = ...
    def get_context(self, request: Any, parent_context: Any): ...

class PageLockedMenuItem(ActionMenuItem):
    name: str = ...
    label: Any = ...
    template: str = ...
    def is_shown(self, request: Any, context: Any): ...
    def get_context(self, request: Any, parent_context: Any): ...

BASE_PAGE_ACTION_MENU_ITEMS: Any

class PageActionMenu:
    template: str = ...
    request: Any = ...
    context: Any = ...
    menu_items: Any = ...
    default_item: Any = ...
    def __init__(self, request: Any, **kwargs: Any): ...
    def render_html(self): ...
    def media(self): ...
