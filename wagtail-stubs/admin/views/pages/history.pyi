from typing import Any, Optional
from wagtail.admin.auth import user_has_any_page_permission as user_has_any_page_permission, user_passes_test as user_passes_test
from wagtail.admin.filters import PageHistoryReportFilterSet as PageHistoryReportFilterSet
from wagtail.admin.views.reports import ReportView as ReportView
from wagtail.core.models import Page as Page, PageLogEntry as PageLogEntry, PageRevision as PageRevision, TaskState as TaskState, UserPagePermissionsProxy as UserPagePermissionsProxy, WorkflowState as WorkflowState

def workflow_history(request: Any, page_id: Any): ...
def workflow_history_detail(request: Any, page_id: Any, workflow_state_id: Any): ...

class PageHistoryView(ReportView):
    template_name: str = ...
    title: Any = ...
    header_icon: str = ...
    paginate_by: int = ...
    filterset_class: Any = ...
    page: Any = ...
    def dispatch(self, request: Any, *args: Any, **kwargs: Any): ...
    def get_context_data(self, *args: Any, object_list: Optional[Any] = ..., **kwargs: Any): ...
    def get_queryset(self): ...