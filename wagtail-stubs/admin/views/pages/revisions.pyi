from typing import Any
from wagtail.admin import messages as messages
from wagtail.admin.action_menu import PageActionMenu as PageActionMenu
from wagtail.admin.auth import user_has_any_page_permission as user_has_any_page_permission, user_passes_test as user_passes_test
from wagtail.admin.views.pages.utils import get_valid_next_url_from_request as get_valid_next_url_from_request
from wagtail.core.models import Page as Page, UserPagePermissionsProxy as UserPagePermissionsProxy

def revisions_index(request: Any, page_id: Any): ...
def revisions_revert(request: Any, page_id: Any, revision_id: Any): ...
def revisions_view(request: Any, page_id: Any, revision_id: Any): ...
def revisions_compare(request: Any, page_id: Any, revision_id_a: Any, revision_id_b: Any): ...
def revisions_unschedule(request: Any, page_id: Any, revision_id: Any): ...
