from rest_framework.filters import BaseFilterBackend
from typing import Any
from wagtail.api.v2.utils import BadRequestError as BadRequestError, parse_boolean as parse_boolean
from wagtail.core import hooks as hooks
from wagtail.core.models import UserPagePermissionsProxy as UserPagePermissionsProxy

class HasChildrenFilter(BaseFilterBackend):
    def filter_queryset(self, request: Any, queryset: Any, view: Any): ...

class ForExplorerFilter(BaseFilterBackend):
    def filter_queryset(self, request: Any, queryset: Any, view: Any): ...
