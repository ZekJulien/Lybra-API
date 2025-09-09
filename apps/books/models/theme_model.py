import uuid
from django.db import models

class Theme(models.Model):
    """Model representing a book theme."""
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    name = models.CharField(
        max_length=255,
        unique=True,
        null=False,
    )
