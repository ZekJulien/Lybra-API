import uuid
from django.db import models

class Author(models.Model):
    '''Model representing an author.'''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255, null=True)
    birthdate = models.DateField(null=True)
