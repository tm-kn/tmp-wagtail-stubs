from typing import Any
from wagtail.admin.menu import Menu as Menu, MenuItem as MenuItem, SubmenuMenuItem as SubmenuMenuItem

class ModelAdminMenuItem(MenuItem):
    model_admin: Any = ...
    def __init__(self, model_admin: Any, order: Any) -> None: ...
    def is_shown(self, request: Any): ...

class GroupMenuItem(SubmenuMenuItem):
    def __init__(self, modeladmingroup: Any, order: Any, menu: Any) -> None: ...
    def is_shown(self, request: Any): ...

class SubMenu(Menu):
    construct_hook_name: Any = ...
    def __init__(self, menuitem_list: Any) -> None: ...
