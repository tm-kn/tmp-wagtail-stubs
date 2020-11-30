from .models import IndexEntry as IndexEntry
from .query import Lexeme as Lexeme, RawSearchQuery as RawSearchQuery
from .utils import get_content_type_pk as get_content_type_pk, get_descendants_content_types_pks as get_descendants_content_types_pks, get_postgresql_connections as get_postgresql_connections, get_sql_weights as get_sql_weights, get_weight as get_weight
from typing import Any, Optional
from wagtail.search.backends.base import BaseSearchBackend as BaseSearchBackend, BaseSearchQueryCompiler as BaseSearchQueryCompiler, BaseSearchResults as BaseSearchResults, FilterFieldError as FilterFieldError
from wagtail.search.index import AutocompleteField as AutocompleteField, RelatedFields as RelatedFields, SearchField as SearchField, get_indexed_models as get_indexed_models
from wagtail.search.query import And as And, Boost as Boost, MatchAll as MatchAll, Not as Not, Or as Or, Phrase as Phrase, PlainText as PlainText
from wagtail.search.utils import ADD as ADD, MUL as MUL, OR as OR

EMPTY_VECTOR: Any

class ObjectIndexer:
    obj: Any = ...
    search_fields: Any = ...
    config: Any = ...
    autocomplete_config: Any = ...
    def __init__(self, obj: Any, backend: Any) -> None: ...
    def prepare_value(self, value: Any): ...
    def prepare_field(self, obj: Any, field: Any) -> None: ...
    def as_vector(self, texts: Any, for_autocomplete: bool = ...): ...
    def id(self): ...
    def title(self): ...
    def body(self): ...
    def autocomplete(self): ...

class Index:
    backend: Any = ...
    name: Any = ...
    db_alias: Any = ...
    connection: Any = ...
    entries: Any = ...
    def __init__(self, backend: Any, db_alias: Optional[Any] = ...) -> None: ...
    def add_model(self, model: Any) -> None: ...
    def refresh(self) -> None: ...
    def delete_stale_model_entries(self, model: Any) -> None: ...
    def delete_stale_entries(self) -> None: ...
    def add_item(self, obj: Any) -> None: ...
    def add_items_upsert(self, content_type_pk: Any, indexers: Any) -> None: ...
    def add_items_update_then_create(self, content_type_pk: Any, indexers: Any) -> None: ...
    def add_items(self, model: Any, objs: Any) -> None: ...
    def delete_item(self, item: Any) -> None: ...

class PostgresSearchQueryCompiler(BaseSearchQueryCompiler):
    DEFAULT_OPERATOR: str = ...
    LAST_TERM_IS_PREFIX: bool = ...
    TARGET_SEARCH_FIELD_TYPE: Any = ...
    sql_weights: Any = ...
    search_fields: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def get_config(self, backend: Any): ...
    def get_search_fields_for_model(self): ...
    def get_search_field(self, field_lookup: Any, fields: Optional[Any] = ...): ...
    def build_tsquery_content(self, query: Any, config: Optional[Any] = ..., invert: bool = ...): ...
    def build_tsquery(self, query: Any, config: Optional[Any] = ...): ...
    def build_tsrank(self, vector: Any, query: Any, config: Optional[Any] = ..., boost: float = ...): ...
    def get_index_vectors(self, search_query: Any): ...
    def get_fields_vectors(self, search_query: Any): ...
    def get_search_vectors(self, search_query: Any): ...
    def search(self, config: Any, start: Any, stop: Any, score_field: Optional[Any] = ...): ...

class PostgresAutocompleteQueryCompiler(PostgresSearchQueryCompiler):
    LAST_TERM_IS_PREFIX: bool = ...
    TARGET_SEARCH_FIELD_TYPE: Any = ...
    def get_config(self, backend: Any): ...
    def get_search_fields_for_model(self): ...
    def get_index_vectors(self, search_query: Any): ...
    def get_fields_vectors(self, search_query: Any): ...

class PostgresSearchResults(BaseSearchResults):
    def get_queryset(self, for_count: bool = ...): ...
    supports_facet: bool = ...
    def facet(self, field_name: Any): ...

class PostgresSearchRebuilder:
    index: Any = ...
    def __init__(self, index: Any) -> None: ...
    def start(self): ...
    def finish(self) -> None: ...

class PostgresSearchAtomicRebuilder(PostgresSearchRebuilder):
    transaction: Any = ...
    transaction_opened: bool = ...
    def __init__(self, index: Any) -> None: ...
    def start(self): ...
    def finish(self) -> None: ...
    def __del__(self) -> None: ...

class PostgresSearchBackend(BaseSearchBackend):
    query_compiler_class: Any = ...
    autocomplete_query_compiler_class: Any = ...
    results_class: Any = ...
    rebuilder_class: Any = ...
    atomic_rebuilder_class: Any = ...
    index_name: Any = ...
    config: Any = ...
    autocomplete_config: Any = ...
    def __init__(self, params: Any) -> None: ...
    def get_index_for_model(self, model: Any, db_alias: Optional[Any] = ...): ...
    def get_index_for_object(self, obj: Any): ...
    def reset_index(self) -> None: ...
    def add_type(self, model: Any) -> None: ...
    def refresh_index(self) -> None: ...
    def add(self, obj: Any) -> None: ...
    def add_bulk(self, model: Any, obj_list: Any) -> None: ...
    def delete(self, obj: Any) -> None: ...
SearchBackend = PostgresSearchBackend
