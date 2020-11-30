from django.core.management.base import BaseCommand
from typing import Any
from wagtail.core.models import Page as Page

class Command(BaseCommand):
    def add_arguments(self, parser: Any) -> None: ...
    def handle(self, *args: Any, **options: Any) -> None: ...
