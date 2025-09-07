from django.db import models
from django.conf import settings

class User(models.Model):
    """Model representing a user with personal and contact information."""
    id = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='user'
    )
    username = models.CharField(
        max_length=150,
        unique=True,
        null=False,
    )
    first_name = models.CharField(
        max_length=100,
        null=True,
    )
    last_name = models.CharField(
        max_length=100,
        null=True,
    )
    street = models.CharField(
        max_length=255,
        null=True,
    )
    postal_code = models.CharField(
        max_length=10,
        null=True,
    )
    city = models.CharField(
        max_length=100,
        null=True,
    )
    xp_total = models.IntegerField(
        default=0
    )
