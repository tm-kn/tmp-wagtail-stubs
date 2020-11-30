from typing import Any
from wagtail.core import hooks as hooks
from wagtail.core.models import PageViewRestriction as PageViewRestriction
from wagtail.core.rich_text.pages import PageLinkHandler as PageLinkHandler

def require_wagtail_login(next: Any): ...
def check_view_restrictions(page: Any, request: Any, serve_args: Any, serve_kwargs: Any): ...
def register_core_features(features: Any) -> None: ...
def register_collection_permissions(): ...
def register_workflow_permissions(): ...
def register_task_permissions(): ...
def describe_collection_children(collection: Any): ...