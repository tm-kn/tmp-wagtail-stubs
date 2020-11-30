from typing import Any
from wagtail.core.models import Collection as Collection, Locale as Locale, Site as Site, Task as Task, Workflow as Workflow
from wagtail.core.permission_policies import ModelPermissionPolicy as ModelPermissionPolicy

site_permission_policy: Any
collection_permission_policy: Any
task_permission_policy: Any
workflow_permission_policy: Any
locale_permission_policy: Any
