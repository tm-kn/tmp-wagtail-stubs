from typing import Any
from wagtail.search.backends.base import BaseSearchBackend as BaseSearchBackend, BaseSearchQueryCompiler as BaseSearchQueryCompiler, BaseSearchResults as BaseSearchResults, FilterFieldError as FilterFieldError
from wagtail.search.index import AutocompleteField as AutocompleteField, FilterField as FilterField, Indexed as Indexed, RelatedFields as RelatedFields, SearchField as SearchField, class_is_indexed as class_is_indexed
from wagtail.search.query import And as And, Boost as Boost, MatchAll as MatchAll, Not as Not, Or as Or, Phrase as Phrase, PlainText as PlainText
from wagtail.utils.utils import deep_update as deep_update

def get_model_root(model: Any): ...

class Elasticsearch2Mapping:
    all_field_name: str = ...
    edgengrams_field_name: str = ...
    type_map: Any = ...
    keyword_type: str = ...
    text_type: str = ...
    set_index_not_analyzed_on_filter_fields: bool = ...
    edgengram_analyzer_config: Any = ...
    model: Any = ...
    def __init__(self, model: Any) -> None: ...
    def get_parent(self): ...
    def get_document_type(self): ...
    def get_field_column_name(self, field: Any): ...
    def get_content_type(self): ...
    def get_all_content_types(self): ...
    def get_field_mapping(self, field: Any): ...
    def get_mapping(self): ...
    def get_document_id(self, obj: Any): ...
    def get_document(self, obj: Any): ...

class Elasticsearch2SearchQueryCompiler(BaseSearchQueryCompiler):
    mapping_class: Any = ...
    DEFAULT_OPERATOR: str = ...
    mapping: Any = ...
    remapped_fields: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def get_inner_query(self): ...
    def get_content_type_filter(self): ...
    def get_filters(self): ...
    def get_query(self): ...
    def get_sort(self): ...

class ElasticsearchAutocompleteQueryCompilerImpl:
    remapped_fields: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def get_inner_query(self): ...

class Elasticsearch2AutocompleteQueryCompiler(Elasticsearch2SearchQueryCompiler, ElasticsearchAutocompleteQueryCompilerImpl): ...

class Elasticsearch2SearchResults(BaseSearchResults):
    fields_param_name: str = ...
    supports_facet: bool = ...
    def facet(self, field_name: Any): ...

class Elasticsearch2Index:
    backend: Any = ...
    es: Any = ...
    mapping_class: Any = ...
    name: Any = ...
    def __init__(self, backend: Any, name: Any) -> None: ...
    def put(self) -> None: ...
    def delete(self) -> None: ...
    def exists(self): ...
    def is_alias(self): ...
    def aliased_indices(self): ...
    def put_alias(self, name: Any) -> None: ...
    def add_model(self, model: Any) -> None: ...
    def add_item(self, item: Any) -> None: ...
    def add_items(self, model: Any, items: Any) -> None: ...
    def delete_item(self, item: Any) -> None: ...
    def refresh(self) -> None: ...
    def reset(self) -> None: ...

class ElasticsearchIndexRebuilder:
    index: Any = ...
    def __init__(self, index: Any) -> None: ...
    def reset_index(self) -> None: ...
    def start(self): ...
    def finish(self) -> None: ...

class ElasticsearchAtomicIndexRebuilder(ElasticsearchIndexRebuilder):
    alias: Any = ...
    index: Any = ...
    def __init__(self, index: Any) -> None: ...
    def reset_index(self) -> None: ...
    def start(self): ...
    def finish(self) -> None: ...

class Elasticsearch2SearchBackend(BaseSearchBackend):
    index_class: Any = ...
    query_compiler_class: Any = ...
    autocomplete_query_compiler_class: Any = ...
    results_class: Any = ...
    mapping_class: Any = ...
    basic_rebuilder_class: Any = ...
    atomic_rebuilder_class: Any = ...
    catch_indexing_errors: bool = ...
    settings: Any = ...
    hosts: Any = ...
    index_name: Any = ...
    timeout: Any = ...
    rebuilder_class: Any = ...
    es: Any = ...
    def __init__(self, params: Any) -> None: ...
    def get_index_for_model(self, model: Any): ...
    def get_index(self): ...
    def get_rebuilder(self): ...
    def reset_index(self) -> None: ...
SearchBackend = Elasticsearch2SearchBackend
