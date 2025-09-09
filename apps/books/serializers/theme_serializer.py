from rest_framework import serializers
from apps.books.models import Theme


class ThemeSerializer(serializers.ModelSerializer):
    """Serializer for the Theme model."""
    class Meta:
        model = Theme
        fields = ['id', 'name']
