from .query import MATCH_NONE as MATCH_NONE, Phrase as Phrase, PlainText as PlainText
from typing import Any, Optional

NOT_SET: Any

def balanced_reduce(operator: Any, seq: Any, initializer: Any = ...): ...

OR: Any
AND: Any
ADD: Any
MUL: Any
MAX_QUERY_STRING_LENGTH: int

def normalise_query_string(query_string: Any): ...
def separate_filters_from_query(query_string: Any): ...
def parse_query_string(query_string: Any, operator: Optional[Any] = ..., zero_terms: Any = ...): ...
