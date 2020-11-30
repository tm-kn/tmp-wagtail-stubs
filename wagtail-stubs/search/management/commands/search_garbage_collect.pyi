from django.core.management.base import BaseCommand
from typing import Any
from wagtail.search import models as models

class Command(BaseCommand):
    def handle(self, **options: Any) -> None: ...
