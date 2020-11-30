from typing import Any
from wagtail.search.index import Indexed as Indexed, RelatedFields as RelatedFields, SearchField as SearchField

def get_postgresql_connections(): ...
def get_descendant_models(model: Any): ...
def get_content_type_pk(model: Any): ...
def get_ancestors_content_types_pks(model: Any): ...
def get_descendants_content_types_pks(model: Any): ...
def get_search_fields(search_fields: Any) -> None: ...

WEIGHTS: str
WEIGHTS_COUNT: Any
BOOSTS_WEIGHTS: Any
WEIGHTS_VALUES: Any

def get_boosts(): ...
def determine_boosts_weights(boosts: Any = ...): ...
def set_weights() -> None: ...
def get_weight(boost: Any): ...
def get_sql_weights(): ...