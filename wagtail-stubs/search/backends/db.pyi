from typing import Any
from wagtail.search.backends.base import BaseSearchBackend as BaseSearchBackend, BaseSearchQueryCompiler as BaseSearchQueryCompiler, BaseSearchResults as BaseSearchResults, FilterFieldError as FilterFieldError
from wagtail.search.query import And as And, Boost as Boost, MatchAll as MatchAll, Not as Not, Or as Or, Phrase as Phrase, PlainText as PlainText
from wagtail.search.utils import AND as AND, OR as OR

MATCH_ALL: str
MATCH_NONE: str

class DatabaseSearchQueryCompiler(BaseSearchQueryCompiler):
    DEFAULT_OPERATOR: str = ...
    OPERATORS: Any = ...
    fields_names: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def get_fields_names(self) -> None: ...
    def build_single_term_filter(self, term: Any): ...
    def check_boost(self, query: Any, boost: float = ...) -> None: ...
    def build_database_filter(self, query: Any, boost: float = ...): ...

class DatabaseSearchResults(BaseSearchResults):
    def get_queryset(self): ...
    supports_facet: bool = ...
    def facet(self, field_name: Any): ...

class DatabaseSearchBackend(BaseSearchBackend):
    query_compiler_class: Any = ...
    results_class: Any = ...
    def reset_index(self) -> None: ...
    def add_type(self, model: Any) -> None: ...
    def refresh_index(self) -> None: ...
    def add(self, obj: Any) -> None: ...
    def add_bulk(self, model: Any, obj_list: Any) -> None: ...
    def delete(self, obj: Any) -> None: ...
SearchBackend = DatabaseSearchBackend