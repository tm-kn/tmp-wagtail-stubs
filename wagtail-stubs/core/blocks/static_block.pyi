from .base import Block
from typing import Any, Optional

class StaticBlock(Block):
    def render_form(self, value: Any, prefix: str = ..., errors: Optional[Any] = ...): ...
    def value_from_datadict(self, data: Any, files: Any, prefix: Any) -> None: ...
    class Meta:
        admin_text: Any = ...
        default: Any = ...
