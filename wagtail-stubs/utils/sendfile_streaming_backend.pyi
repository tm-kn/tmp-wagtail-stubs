from typing import Any, Optional

def sendfile(request: Any, filename: Any, **kwargs: Any): ...
def was_modified_since(header: Optional[Any] = ..., mtime: int = ..., size: int = ...): ...