from modelcluster.forms import ClusterForm, ClusterFormMetaclass
from typing import Any
from wagtail.admin import widgets as widgets
from wagtail.admin.forms.tags import TagField as TagField

FORM_FIELD_OVERRIDES: Any
DIRECT_FORM_FIELD_OVERRIDES: Any

def formfield_for_dbfield(db_field: Any, **kwargs: Any): ...

class WagtailAdminModelFormMetaclass(ClusterFormMetaclass):
    extra_form_count: int = ...
    def __new__(cls, name: Any, bases: Any, attrs: Any): ...
    @classmethod
    def child_form(cls): ...

class WagtailAdminModelForm(ClusterForm, metaclass=WagtailAdminModelFormMetaclass):
    @property
    def media(self): ...
