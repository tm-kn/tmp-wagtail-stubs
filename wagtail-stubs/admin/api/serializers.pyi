from rest_framework.fields import Field
from typing import Any
from wagtail.api.v2.serializers import PageSerializer as PageSerializer, get_serializer_class as get_serializer_class
from wagtail.api.v2.utils import get_full_url as get_full_url
from wagtail.core.models import Page as Page

def get_model_listing_url(context: Any, model: Any): ...

class PageStatusField(Field):
    def get_attribute(self, instance: Any): ...
    def to_representation(self, page: Any): ...

class PageChildrenField(Field):
    def get_attribute(self, instance: Any): ...
    def to_representation(self, page: Any): ...

class PageDescendantsField(Field):
    def get_attribute(self, instance: Any): ...
    def to_representation(self, page: Any): ...

class PageAncestorsField(Field):
    def get_attribute(self, instance: Any): ...
    def to_representation(self, page: Any): ...

class PageTranslationsField(Field):
    def get_attribute(self, instance: Any): ...
    def to_representation(self, page: Any): ...

class AdminPageSerializer(PageSerializer):
    status: Any = ...
    children: Any = ...
    descendants: Any = ...
    ancestors: Any = ...
    translations: Any = ...
    admin_display_title: Any = ...