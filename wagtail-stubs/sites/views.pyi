from typing import Any
from wagtail.admin.views import generic as generic
from wagtail.admin.viewsets.model import ModelViewSet as ModelViewSet
from wagtail.core.models import Site as Site
from wagtail.core.permissions import site_permission_policy as site_permission_policy
from wagtail.sites.forms import SiteForm as SiteForm

class IndexView(generic.IndexView):
    template_name: str = ...
    page_title: Any = ...
    add_item_label: Any = ...
    context_object_name: str = ...

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

class DeleteView(generic.DeleteView):
    success_message: Any = ...
    page_title: Any = ...
    confirmation_message: Any = ...

class SiteViewSet(ModelViewSet):
    icon: str = ...
    model: Any = ...
    permission_policy: Any = ...
    index_view_class: Any = ...
    add_view_class: Any = ...
    edit_view_class: Any = ...
    delete_view_class: Any = ...
    def get_form_class(self, for_update: bool = ...): ...
