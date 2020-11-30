from typing import Any
from wagtail.admin.userbar import AddPageItem as AddPageItem, ApproveModerationEditPageItem as ApproveModerationEditPageItem, EditPageItem as EditPageItem, RejectModerationEditPageItem as RejectModerationEditPageItem
from wagtail.core import hooks as hooks
from wagtail.core.models import Page as Page, PageRevision as PageRevision

def for_frontend(request: Any, page_id: Any): ...
def for_moderation(request: Any, revision_id: Any): ...
