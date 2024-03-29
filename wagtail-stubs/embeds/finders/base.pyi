from typing import Any, Optional

class EmbedFinder:
    def accept(self, url: Any): ...
    def find_embed(self, url: Any, max_width: Optional[Any] = ...) -> None: ...
