from typing import Any
from wagtail.admin import messages as messages
from wagtail.admin.auth import PermissionPolicyChecker as PermissionPolicyChecker
from wagtail.admin.forms.search import SearchForm as SearchForm
from wagtail.admin.models import popular_tags_for_model as popular_tags_for_model
from wagtail.core.models import Collection as Collection
from wagtail.documents import get_document_model as get_document_model
from wagtail.documents.forms import get_document_form as get_document_form
from wagtail.documents.permissions import permission_policy as permission_policy

permission_checker: Any

def index(request: Any): ...
def add(request: Any): ...
def edit(request: Any, document_id: Any): ...
def delete(request: Any, document_id: Any): ...
def usage(request: Any, document_id: Any): ...
