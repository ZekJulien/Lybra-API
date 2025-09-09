import uuid
from django.db import models

class Collection(models.Model):
    """Model representing a book collection."""
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    name = models.CharField(
        max_length=255,
        null=False,
        unique=True,
    )
    description = models.TextField(
        null=True,
    )
