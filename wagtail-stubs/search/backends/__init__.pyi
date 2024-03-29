from django.core.exceptions import ImproperlyConfigured
from typing import Any

class InvalidSearchBackendError(ImproperlyConfigured): ...

def get_search_backend_config(): ...
def import_backend(dotted_path: Any): ...
def get_search_backend(backend: str = ..., **kwargs: Any): ...
def get_search_backends_with_name(with_auto_update: bool = ...) -> None: ...
def get_search_backends(with_auto_update: bool = ...): ...
