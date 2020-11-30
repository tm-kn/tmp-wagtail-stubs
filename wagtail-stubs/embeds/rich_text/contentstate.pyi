from typing import Any
from wagtail.admin.rich_text.converters.contentstate_models import Entity as Entity
from wagtail.admin.rich_text.converters.html_to_contentstate import AtomicBlockEntityElementHandler as AtomicBlockEntityElementHandler
from wagtail.embeds import embeds as embeds
from wagtail.embeds.exceptions import EmbedException as EmbedException

def media_embed_entity(props: Any): ...

class MediaEmbedElementHandler(AtomicBlockEntityElementHandler):
    def create_entity(self, name: Any, attrs: Any, state: Any, contentstate: Any): ...

ContentstateMediaConversionRule: Any
