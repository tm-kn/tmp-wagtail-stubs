from typing import Any, Optional
from wagtail.admin.auth import user_has_any_page_permission as user_has_any_page_permission, user_passes_test as user_passes_test
from wagtail.admin.navigation import get_explorable_root_page as get_explorable_root_page
from wagtail.core import hooks as hooks
from wagtail.core.models import Page as Page, UserPagePermissionsProxy as UserPagePermissionsProxy

def index(request: Any, parent_page_id: Optional[Any] = ...): ...
