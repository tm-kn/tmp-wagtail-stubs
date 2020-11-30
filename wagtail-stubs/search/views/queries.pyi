from typing import Any
from wagtail.admin.forms.search import SearchForm as SearchForm
from wagtail.admin.modal_workflow import render_modal_workflow as render_modal_workflow
from wagtail.search import models as models
from wagtail.search.utils import normalise_query_string as normalise_query_string

def chooser(request: Any, get_results: bool = ...): ...
def chooserresults(request: Any): ...
