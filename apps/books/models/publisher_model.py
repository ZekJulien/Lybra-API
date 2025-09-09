import uuid
from django.db import models
from django_countries.fields import CountryField

class Publisher(models.Model):
    """Model representing a book publisher."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False, unique=True)
    country = CountryField(null=True)
    creation_date = models.DateField(null=True)
    website = models.TextField(null=True)