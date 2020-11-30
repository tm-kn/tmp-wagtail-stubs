from typing import Any
from wagtail.admin.navigation import get_site_for_user as get_site_for_user
from wagtail.admin.site_summary import SiteSummaryPanel as SiteSummaryPanel
from wagtail.core import hooks as hooks
from wagtail.core.models import Page as Page, PageRevision as PageRevision, TaskState as TaskState, UserPagePermissionsProxy as UserPagePermissionsProxy, WorkflowState as WorkflowState

User: Any

class UpgradeNotificationPanel:
    name: str = ...
    order: int = ...
    request: Any = ...
    def __init__(self, request: Any) -> None: ...
    def render(self): ...

class IE11WarningPanel:
    name: str = ...
    order: int = ...
    request: Any = ...
    def __init__(self, request: Any) -> None: ...
    def render(self): ...

class PagesForModerationPanel:
    name: str = ...
    order: int = ...
    request: Any = ...
    page_revisions_for_moderation: Any = ...
    def __init__(self, request: Any) -> None: ...
    def render(self): ...

class UserPagesInWorkflowModerationPanel:
    name: str = ...
    order: int = ...
    request: Any = ...
    workflow_states: Any = ...
    def __init__(self, request: Any) -> None: ...
    def render(self): ...

class WorkflowPagesToModeratePanel:
    name: str = ...
    order: int = ...
    request: Any = ...
    states: Any = ...
    def __init__(self, request: Any) -> None: ...
    def render(self): ...

class LockedPagesPanel:
    name: str = ...
    order: int = ...
    request: Any = ...
    def __init__(self, request: Any) -> None: ...
    def render(self): ...

class RecentEditsPanel:
    name: str = ...
    order: int = ...
    request: Any = ...
    last_edits: Any = ...
    def __init__(self, request: Any) -> None: ...
    def render(self): ...

def home(request: Any): ...
def error_test(request: Any) -> None: ...
def default(request: Any) -> None: ...
def icons(): ...
def sprite(request: Any): ...