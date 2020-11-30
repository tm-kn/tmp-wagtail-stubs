from typing import Any
from wagtail.admin.forms.search import SearchForm as SearchForm
from wagtail.admin.modal_workflow import render_modal_workflow as render_modal_workflow
from wagtail.search.backends import get_search_backend as get_search_backend
from wagtail.search.index import class_is_indexed as class_is_indexed
from wagtail.snippets.views.snippets import get_snippet_model_from_url_params as get_snippet_model_from_url_params

def choose(request: Any, app_label: Any, model_name: Any): ...
def chosen(request: Any, app_label: Any, model_name: Any, pk: Any): ...
