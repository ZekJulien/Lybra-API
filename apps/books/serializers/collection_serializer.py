from rest_framework import serializers

from apps.books.models import Collection

class CollectionSerializer(serializers.ModelSerializer):
    """Serializer for the Collection model."""
    class Meta:
        model = Collection
        fields = ['id', 'name', 'description']
