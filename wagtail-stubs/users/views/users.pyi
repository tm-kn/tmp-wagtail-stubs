from typing import Any
from wagtail.admin import messages as messages
from wagtail.admin.auth import any_permission_required as any_permission_required, permission_required as permission_required
from wagtail.admin.forms.search import SearchForm as SearchForm
from wagtail.core import hooks as hooks
from wagtail.core.compat import AUTH_USER_APP_LABEL as AUTH_USER_APP_LABEL, AUTH_USER_MODEL_NAME as AUTH_USER_MODEL_NAME
from wagtail.users.forms import UserCreationForm as UserCreationForm, UserEditForm as UserEditForm
from wagtail.users.utils import user_can_delete_user as user_can_delete_user
from wagtail.utils.loading import get_custom_form as get_custom_form

User: Any
add_user_perm: Any
change_user_perm: Any
delete_user_perm: Any

def get_user_creation_form(): ...
def get_user_edit_form(): ...
def index(request: Any, *args: Any): ...
def create(request: Any): ...
def edit(request: Any, user_id: Any): ...
def delete(request: Any, user_id: Any): ...
