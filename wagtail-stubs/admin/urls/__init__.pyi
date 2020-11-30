from typing import Any
from wagtail.admin.auth import require_admin_access as require_admin_access
from wagtail.admin.views import account as account, chooser as chooser, home as home, tags as tags, userbar as userbar
from wagtail.admin.views.pages import listing as listing
from wagtail.core import hooks as hooks
from wagtail.utils.urlpatterns import decorate_urlpatterns as decorate_urlpatterns

urlpatterns: Any
urls: Any
sprite_hash: Any

def get_sprite_hash(): ...
def display_custom_404(view_func: Any): ...
