from drf_spectacular.utils import extend_schema
from rest_framework import serializers

from apps.books.models import Author

class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for the Author model."""
    class Meta:
        model = Author
        fields = ['id', 'name', 'nationality', 'birthdate']
