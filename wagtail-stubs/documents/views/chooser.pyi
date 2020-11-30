from typing import Any
from wagtail.admin.auth import PermissionPolicyChecker as PermissionPolicyChecker
from wagtail.admin.forms.search import SearchForm as SearchForm
from wagtail.admin.modal_workflow import render_modal_workflow as render_modal_workflow
from wagtail.core import hooks as hooks
from wagtail.core.models import Collection as Collection
from wagtail.documents import get_document_model as get_document_model
from wagtail.documents.forms import get_document_form as get_document_form
from wagtail.documents.permissions import permission_policy as permission_policy

permission_checker: Any

def get_chooser_context(): ...
def get_document_result_data(document: Any): ...
def chooser(request: Any): ...
def document_chosen(request: Any, document_id: Any): ...
def chooser_upload(request: Any): ...
