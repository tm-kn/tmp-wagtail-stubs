from .sitemap_generator import Sitemap as Sitemap
from typing import Any, Optional

def index(request: Any, sitemaps: Any, **kwargs: Any): ...
def sitemap(request: Any, sitemaps: Optional[Any] = ..., **kwargs: Any): ...
def prepare_sitemaps(request: Any, sitemaps: Any): ...
