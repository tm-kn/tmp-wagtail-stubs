from typing import Any

register: Any

def items_for_result(view: Any, result: Any) -> None: ...
def results(view: Any, object_list: Any) -> None: ...
def result_list(context: Any): ...
def pagination_link_previous(current_page: Any, view: Any): ...
def pagination_link_next(current_page: Any, view: Any): ...
def search_form(context: Any): ...
def admin_list_filter(view: Any, spec: Any): ...
def result_row_display(context: Any, index: Any): ...
def result_row_value_display(context: Any, index: Any): ...
def get_content_type_for_obj(obj: Any): ...
def prepopulated_slugs(context: Any): ...
