from ..fields import ImageRenditionField as ImageRenditionField
from ..v2.serializers import ImageSerializer as ImageSerializer
from typing import Any

class AdminImageSerializer(ImageSerializer):
    thumbnail: Any = ...
