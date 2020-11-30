from typing import Any, Optional
from wagtail.search.index import class_is_indexed as class_is_indexed, get_indexed_models as get_indexed_models
from wagtail.search.query import MATCH_ALL as MATCH_ALL, PlainText as PlainText

class FilterError(Exception): ...

class FieldError(Exception):
    field_name: Any = ...
    def __init__(self, *args: Any, field_name: Optional[Any] = ..., **kwargs: Any) -> None: ...

class SearchFieldError(FieldError): ...
class FilterFieldError(FieldError): ...
class OrderByFieldError(FieldError): ...

class BaseSearchQueryCompiler:
    DEFAULT_OPERATOR: str = ...
    queryset: Any = ...
    query: Any = ...
    fields: Any = ...
    order_by_relevance: Any = ...
    partial_match: Any = ...
    def __init__(self, queryset: Any, query: Any, fields: Optional[Any] = ..., operator: Optional[Any] = ..., order_by_relevance: bool = ..., partial_match: bool = ...) -> None: ...
    def check(self) -> None: ...

class BaseSearchResults:
    supports_facet: bool = ...
    backend: Any = ...
    query_compiler: Any = ...
    prefetch_related: Any = ...
    start: int = ...
    stop: Any = ...
    def __init__(self, backend: Any, query_compiler: Any, prefetch_related: Optional[Any] = ...) -> None: ...
    def results(self): ...
    def count(self): ...
    def __getitem__(self, key: Any): ...
    def __iter__(self) -> Any: ...
    def __len__(self): ...
    def annotate_score(self, field_name: Any): ...
    def facet(self, field_name: Any) -> None: ...

class EmptySearchResults(BaseSearchResults):
    def __init__(self) -> None: ...

class NullIndex:
    def add_model(self, model: Any) -> None: ...
    def refresh(self) -> None: ...
    def add_item(self, item: Any) -> None: ...
    def add_items(self, model: Any, items: Any) -> None: ...
    def delete_item(self, item: Any) -> None: ...

class BaseSearchBackend:
    query_compiler_class: Any = ...
    autocomplete_query_compiler_class: Any = ...
    results_class: Any = ...
    rebuilder_class: Any = ...
    catch_indexing_errors: bool = ...
    def __init__(self, params: Any) -> None: ...
    def get_index_for_model(self, model: Any): ...
    def get_rebuilder(self) -> None: ...
    def reset_index(self) -> None: ...
    def add_type(self, model: Any) -> None: ...
    def refresh_index(self) -> None: ...
    def add(self, obj: Any) -> None: ...
    def add_bulk(self, model: Any, obj_list: Any) -> None: ...
    def delete(self, obj: Any) -> None: ...
    def search(self, query: Any, model_or_queryset: Any, fields: Optional[Any] = ..., operator: Optional[Any] = ..., order_by_relevance: bool = ..., partial_match: bool = ...): ...
    def autocomplete(self, query: Any, model_or_queryset: Any, fields: Optional[Any] = ..., operator: Optional[Any] = ..., order_by_relevance: bool = ...): ...
