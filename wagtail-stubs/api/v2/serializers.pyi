from .utils import get_object_detail_url as get_object_detail_url
from rest_framework import relations, serializers
from rest_framework.fields import Field
from typing import Any, Optional

class TypeField(Field):
    def get_attribute(self, instance: Any): ...
    def to_representation(self, obj: Any): ...

class DetailUrlField(Field):
    def get_attribute(self, instance: Any): ...
    def to_representation(self, url: Any): ...

class PageHtmlUrlField(Field):
    def get_attribute(self, instance: Any): ...
    def to_representation(self, page: Any): ...

class PageTypeField(Field):
    def get_attribute(self, instance: Any): ...
    def to_representation(self, page: Any): ...

class PageLocaleField(Field):
    def get_attribute(self, instance: Any): ...
    def to_representation(self, page: Any): ...

class RelatedField(relations.RelatedField):
    serializer_class: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def to_representation(self, value: Any): ...

class PageParentField(relations.RelatedField):
    def get_attribute(self, instance: Any): ...
    def to_representation(self, value: Any): ...

class ChildRelationField(Field):
    serializer_class: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def to_representation(self, value: Any): ...

class StreamField(Field):
    def to_representation(self, value: Any): ...

class TagsField(Field):
    def to_representation(self, value: Any): ...

class BaseSerializer(serializers.ModelSerializer):
    serializer_field_mapping: Any = ...
    serializer_related_field: Any = ...
    type: Any = ...
    detail_url: Any = ...
    def to_representation(self, instance: Any): ...
    def build_property_field(self, field_name: Any, model_class: Any): ...
    def build_relational_field(self, field_name: Any, relation_info: Any): ...

class PageSerializer(BaseSerializer):
    type: Any = ...
    locale: Any = ...
    html_url: Any = ...
    parent: Any = ...
    def build_relational_field(self, field_name: Any, relation_info: Any): ...

def get_serializer_class(model: Any, field_names: Any, meta_fields: Any, field_serializer_overrides: Optional[Any] = ..., child_serializer_classes: Optional[Any] = ..., base: Any = ...): ...