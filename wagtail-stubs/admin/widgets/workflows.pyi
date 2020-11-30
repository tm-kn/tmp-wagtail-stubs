from typing import Any
from wagtail.admin.staticfiles import versioned_static as versioned_static
from wagtail.admin.widgets import AdminChooser as AdminChooser
from wagtail.core.models import Task as Task

class AdminTaskChooser(AdminChooser):
    choose_one_text: Any = ...
    choose_another_text: Any = ...
    link_to_chosen_text: Any = ...
    def render_html(self, name: Any, value: Any, attrs: Any): ...
    def render_js_init(self, id_: Any, name: Any, value: Any): ...
    @property
    def media(self): ...