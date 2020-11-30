from typing import Any

FIND_A_TAG: Any
FIND_EMBED_TAG: Any
FIND_ATTRS: Any

def extract_attrs(attr_string: Any): ...

class EmbedRewriter:
    embed_rules: Any = ...
    def __init__(self, embed_rules: Any) -> None: ...
    def replace_tag(self, match: Any): ...
    def __call__(self, html: Any): ...

class LinkRewriter:
    link_rules: Any = ...
    def __init__(self, link_rules: Any) -> None: ...
    def replace_tag(self, match: Any): ...
    def __call__(self, html: Any): ...

class MultiRuleRewriter:
    rewriters: Any = ...
    def __init__(self, rewriters: Any) -> None: ...
    def __call__(self, html: Any): ...
