from typing import Any, Optional
from wagtail.admin import messages as messages
from wagtail.core import hooks as hooks
from wagtail.core.models import Page as Page

def move_choose_destination(request: Any, page_to_move_id: Any, viewed_page_id: Optional[Any] = ...): ...
def move_confirm(request: Any, page_to_move_id: Any, destination_id: Any): ...
