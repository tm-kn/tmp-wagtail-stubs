from typing import Any
from wagtail.admin.userbar import AddPageItem as AddPageItem, AdminItem as AdminItem, ApproveModerationEditPageItem as ApproveModerationEditPageItem, EditPageItem as EditPageItem, ExplorePageItem as ExplorePageItem, RejectModerationEditPageItem as RejectModerationEditPageItem
from wagtail.core import hooks as hooks
from wagtail.core.models import PAGE_TEMPLATE_VAR as PAGE_TEMPLATE_VAR, Page as Page, PageRevision as PageRevision
from wagtail.users.models import UserProfile as UserProfile

register: Any

def get_page_instance(context: Any): ...
def wagtailuserbar(context: Any, position: str = ...): ...
