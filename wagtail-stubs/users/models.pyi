from django.db import models
from typing import Any

def upload_avatar_to(instance: Any, filename: Any): ...

class UserProfile(models.Model):
    user: Any = ...
    submitted_notifications: Any = ...
    approved_notifications: Any = ...
    rejected_notifications: Any = ...
    preferred_language: Any = ...
    current_time_zone: Any = ...
    avatar: Any = ...
    @classmethod
    def get_for_user(cls, user: Any): ...
    def get_preferred_language(self): ...
    def get_current_time_zone(self): ...
    class Meta:
        verbose_name: Any = ...
        verbose_name_plural: Any = ...
