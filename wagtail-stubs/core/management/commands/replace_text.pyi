from django.core.management.base import BaseCommand
from typing import Any
from wagtail.core.models import PageRevision as PageRevision, get_page_models as get_page_models

def replace_in_model(model: Any, from_text: Any, to_text: Any) -> None: ...

class Command(BaseCommand):
    def add_arguments(self, parser: Any) -> None: ...
    def handle(self, *args: Any, **options: Any) -> None: ...
