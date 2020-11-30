from typing import Any
from wagtail.core.rich_text import LinkHandler as LinkHandler
from wagtail.documents import get_document_model as get_document_model

class DocumentLinkHandler(LinkHandler):
    identifier: str = ...
    @staticmethod
    def get_model(): ...
    @classmethod
    def expand_db_attributes(cls, attrs: Any): ...
