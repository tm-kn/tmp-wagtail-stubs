from typing import Any
from wagtail.core.compat import AUTH_USER_APP_LABEL as AUTH_USER_APP_LABEL, AUTH_USER_MODEL_NAME as AUTH_USER_MODEL_NAME

delete_user_perm: Any

def user_can_delete_user(current_user: Any, user_to_delete: Any): ...
def get_gravatar_url(email: Any, size: int = ...): ...
