from django_countries.serializer_fields import CountryField
from rest_framework import serializers
from apps.books.models import Publisher

class PublisherSerializer(serializers.ModelSerializer):
    """Serializer for the Publisher model."""
    country = CountryField()

    class Meta:
        model = Publisher
        fields = ['id', 'name', 'country', 'creation_date', 'website']
