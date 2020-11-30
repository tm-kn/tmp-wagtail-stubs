from typing import Any
from wagtail.admin.auth import user_has_any_page_permission as user_has_any_page_permission, user_passes_test as user_passes_test
from wagtail.admin.forms.search import SearchForm as SearchForm
from wagtail.core.models import Page as Page
from wagtail.search.query import MATCH_ALL as MATCH_ALL
from wagtail.search.utils import parse_query_string as parse_query_string

def search(request: Any): ...
