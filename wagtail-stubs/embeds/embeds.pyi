from .exceptions import EmbedUnsupportedProviderException as EmbedUnsupportedProviderException
from .finders import get_finders as get_finders
from .models import Embed as Embed
from typing import Any, Optional

def get_embed(url: Any, max_width: Optional[Any] = ..., finder: Optional[Any] = ...): ...
