from .. import get_document_model as get_document_model
from ..forms import get_document_form as get_document_form, get_document_multi_form as get_document_multi_form
from ..permissions import permission_policy as permission_policy
from typing import Any, Optional
from wagtail.admin.auth import PermissionPolicyChecker as PermissionPolicyChecker
from wagtail.search.backends import get_search_backends as get_search_backends

permission_checker: Any

def add(request: Any): ...
def edit(request: Any, doc_id: Any, callback: Optional[Any] = ...): ...
def delete(request: Any, doc_id: Any): ...
