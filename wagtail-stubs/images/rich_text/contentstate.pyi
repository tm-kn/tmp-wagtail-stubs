from typing import Any
from wagtail.admin.rich_text.converters.contentstate_models import Entity as Entity
from wagtail.admin.rich_text.converters.html_to_contentstate import AtomicBlockEntityElementHandler as AtomicBlockEntityElementHandler
from wagtail.images import get_image_model as get_image_model
from wagtail.images.formats import get_image_format as get_image_format
from wagtail.images.shortcuts import get_rendition_or_not_found as get_rendition_or_not_found

def image_entity(props: Any): ...

class ImageElementHandler(AtomicBlockEntityElementHandler):
    def create_entity(self, name: Any, attrs: Any, state: Any, contentstate: Any): ...

ContentstateImageConversionRule: Any
