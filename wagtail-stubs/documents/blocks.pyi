from typing import Any, Optional
from wagtail.core.blocks import ChooserBlock as ChooserBlock

class DocumentChooserBlock(ChooserBlock):
    def target_model(self): ...
    def widget(self): ...
    def render_basic(self, value: Any, context: Optional[Any] = ...): ...
    class Meta:
        icon: str = ...