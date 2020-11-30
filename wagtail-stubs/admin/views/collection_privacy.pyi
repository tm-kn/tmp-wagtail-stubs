from typing import Any
from wagtail.admin.forms.collections import CollectionViewRestrictionForm as CollectionViewRestrictionForm
from wagtail.admin.modal_workflow import render_modal_workflow as render_modal_workflow
from wagtail.core.models import Collection as Collection, CollectionViewRestriction as CollectionViewRestriction
from wagtail.core.permissions import collection_permission_policy as collection_permission_policy

def set_privacy(request: Any, collection_id: Any): ...
