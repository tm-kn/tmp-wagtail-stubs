from typing import Any
from wagtail.core import hooks as hooks

class FeatureRegistry:
    has_scanned_for_features: bool = ...
    plugins_by_editor: Any = ...
    default_features: Any = ...
    link_types: Any = ...
    embed_types: Any = ...
    converter_rules_by_converter: Any = ...
    def __init__(self) -> None: ...
    def get_default_features(self): ...
    def register_editor_plugin(self, editor_name: Any, feature_name: Any, plugin: Any) -> None: ...
    def get_editor_plugin(self, editor_name: Any, feature_name: Any): ...
    def register_link_type(self, handler: Any) -> None: ...
    def get_link_types(self): ...
    def register_embed_type(self, handler: Any) -> None: ...
    def get_embed_types(self): ...
    def register_converter_rule(self, converter_name: Any, feature_name: Any, rule: Any) -> None: ...
    def get_converter_rule(self, converter_name: Any, feature_name: Any): ...
    @staticmethod
    def function_as_entity_handler(identifier: Any, fn: Any): ...
