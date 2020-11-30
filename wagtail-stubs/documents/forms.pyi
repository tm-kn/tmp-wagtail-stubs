from typing import Any
from wagtail.admin import widgets as widgets
from wagtail.admin.forms.collections import BaseCollectionMemberForm as BaseCollectionMemberForm, CollectionChoiceField as CollectionChoiceField, collection_member_permission_formset_factory as collection_member_permission_formset_factory
from wagtail.core.models import Collection as Collection
from wagtail.documents.models import Document as Document

def formfield_for_dbfield(db_field: Any, **kwargs: Any): ...

class BaseDocumentForm(BaseCollectionMemberForm):
    permission_policy: Any = ...

def get_document_form(model: Any): ...
def get_document_multi_form(model: Any): ...

GroupDocumentPermissionFormSet: Any
