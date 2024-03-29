from typing import Any, Optional

ELEMENT_SELECTOR: Any
ELEMENT_WITH_ATTR_SELECTOR: Any
ELEMENT_WITH_ATTR_EXACT_SINGLE_QUOTE_SELECTOR: Any
ELEMENT_WITH_ATTR_EXACT_DOUBLE_QUOTE_SELECTOR: Any
ELEMENT_WITH_ATTR_EXACT_UNQUOTED_SELECTOR: Any

class HTMLRuleset:
    element_rules: Any = ...
    def __init__(self, rules: Optional[Any] = ...) -> None: ...
    def add_rules(self, rules: Any) -> None: ...
    def add_rule(self, selector: Any, result: Any) -> None: ...
    def match(self, name: Any, attrs: Any): ...
