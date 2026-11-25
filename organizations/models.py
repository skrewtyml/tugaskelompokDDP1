import secrets

from django.conf import settings
from django.db import models


def generate_invite_code():
    return secrets.token_urlsafe(6)


class Workspace(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    invite_code = models.CharField(
        max_length=20, unique=True, default=generate_invite_code
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="created_workspaces",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name