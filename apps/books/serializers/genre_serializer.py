from rest_framework import serializers
from apps.books.models import Genre

class GenreSerializer(serializers.ModelSerializer):
    """Serializer for the Genre model."""
    class Meta:
        model = Genre
        fields = ['id', 'name']