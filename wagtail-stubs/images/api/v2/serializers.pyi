from rest_framework.fields import Field
from typing import Any
from wagtail.api.v2.serializers import BaseSerializer as BaseSerializer

class ImageDownloadUrlField(Field):
    def get_attribute(self, instance: Any): ...
    def to_representation(self, image: Any): ...

class ImageSerializer(BaseSerializer):
    download_url: Any = ...
