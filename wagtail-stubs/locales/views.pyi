from .forms import LocaleForm as LocaleForm
from .utils import get_locale_usage as get_locale_usage
from typing import Any, Optional
from wagtail.admin import messages as messages
from wagtail.admin.views import generic as generic
from wagtail.admin.viewsets.model import ModelViewSet as ModelViewSet
from wagtail.core.models import Locale as Locale
from wagtail.core.permissions import locale_permission_policy as locale_permission_policy

class IndexView(generic.IndexView):
    template_name: str = ...
    page_title: Any = ...
    add_item_label: Any = ...
    context_object_name: str = ...
    queryset: Any = ...
    def get_context_data(self): ...

class CreateView(generic.CreateView):
    page_title: Any = ...
    success_message: Any = ...
    template_name: str = ...

class EditView(generic.EditView):
    success_message: Any = ...
    error_message: Any = ...
    delete_item_label: Any = ...
    context_object_name: str = ...
    template_name: str = ...
    queryset: Any = ...

class DeleteView(generic.DeleteView):
    success_message: Any = ...
    page_title: Any = ...
    confirmation_message: Any = ...
    template_name: str = ...
    queryset: Any = ...
    cannot_delete_message: Any = ...
    def can_delete(self, locale: Any): ...
    def get_context_data(self, object: Optional[Any] = ...): ...
    def delete(self, request: Any, *args: Any, **kwargs: Any): ...

class LocaleViewSet(ModelViewSet):
    icon: str = ...
    model: Any = ...
    permission_policy: Any = ...
    index_view_class: Any = ...
    add_view_class: Any = ...
    edit_view_class: Any = ...
    delete_view_class: Any = ...
    def get_form_class(self, for_update: bool = ...): ...