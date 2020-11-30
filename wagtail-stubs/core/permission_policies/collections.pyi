from .base import BaseDjangoAuthPermissionPolicy as BaseDjangoAuthPermissionPolicy
from typing import Any, Optional
from wagtail.core.models import Collection as Collection, GroupCollectionPermission as GroupCollectionPermission

class CollectionPermissionLookupMixin:
    def collections_user_has_permission_for(self, user: Any, action: Any): ...

class CollectionPermissionPolicy(CollectionPermissionLookupMixin, BaseDjangoAuthPermissionPolicy):
    def user_has_permission(self, user: Any, action: Any): ...
    def user_has_any_permission(self, user: Any, actions: Any): ...
    def users_with_any_permission(self, actions: Any): ...
    def user_has_permission_for_instance(self, user: Any, action: Any, instance: Any): ...
    def user_has_any_permission_for_instance(self, user: Any, actions: Any, instance: Any): ...
    def instances_user_has_any_permission_for(self, user: Any, actions: Any): ...
    def users_with_any_permission_for_instance(self, actions: Any, instance: Any): ...
    def collections_user_has_any_permission_for(self, user: Any, actions: Any): ...

class CollectionOwnershipPermissionPolicy(CollectionPermissionLookupMixin, BaseDjangoAuthPermissionPolicy):
    owner_field_name: Any = ...
    def __init__(self, model: Any, auth_model: Optional[Any] = ..., owner_field_name: str = ...) -> None: ...
    def user_has_permission(self, user: Any, action: Any): ...
    def users_with_any_permission(self, actions: Any): ...
    def user_has_permission_for_instance(self, user: Any, action: Any, instance: Any): ...
    def user_has_any_permission_for_instance(self, user: Any, actions: Any, instance: Any): ...
    def instances_user_has_any_permission_for(self, user: Any, actions: Any): ...
    def users_with_any_permission_for_instance(self, actions: Any, instance: Any): ...
    def collections_user_has_any_permission_for(self, user: Any, actions: Any): ...
