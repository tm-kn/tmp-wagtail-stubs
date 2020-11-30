from .utils import BadRequestError as BadRequestError, parse_boolean as parse_boolean
from rest_framework.filters import BaseFilterBackend
from typing import Any
from wagtail.core.models import Locale as Locale, Page as Page
from wagtail.search.backends import get_search_backend as get_search_backend
from wagtail.search.backends.base import FilterFieldError as FilterFieldError, OrderByFieldError as OrderByFieldError

class FieldsFilter(BaseFilterBackend):
    def filter_queryset(self, request: Any, queryset: Any, view: Any): ...

class OrderingFilter(BaseFilterBackend):
    def filter_queryset(self, request: Any, queryset: Any, view: Any): ...

class SearchFilter(BaseFilterBackend):
    def filter_queryset(self, request: Any, queryset: Any, view: Any): ...

class ChildOfFilter(BaseFilterBackend):
    def filter_queryset(self, request: Any, queryset: Any, view: Any): ...

class DescendantOfFilter(BaseFilterBackend):
    def filter_queryset(self, request: Any, queryset: Any, view: Any): ...

class TranslationOfFilter(BaseFilterBackend):
    def filter_queryset(self, request: Any, queryset: Any, view: Any): ...

class LocaleFilter(BaseFilterBackend):
    def filter_queryset(self, request: Any, queryset: Any, view: Any): ...
