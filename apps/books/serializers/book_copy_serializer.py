from rest_framework import serializers
from apps.books.models import BookCopy

class BookCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCopy
        fields = ['book', 'status', 'location', 'is_active']
