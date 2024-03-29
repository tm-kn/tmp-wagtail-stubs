from django.core.management.base import BaseCommand
from typing import Any
from wagtail.search.backends import get_search_backend as get_search_backend
from wagtail.search.index import get_indexed_models as get_indexed_models

DEFAULT_CHUNK_SIZE: int

def group_models_by_index(backend: Any, models: Any): ...

class Command(BaseCommand):
    def update_backend(self, backend_name: Any, schema_only: bool = ..., chunk_size: Any = ...) -> None: ...
    def add_arguments(self, parser: Any) -> None: ...
    def handle(self, **options: Any) -> None: ...
    def print_newline(self) -> None: ...
    def print_iter_progress(self, iterable: Any) -> None: ...
    def queryset_chunks(self, qs: Any, chunk_size: Any = ...) -> None: ...
