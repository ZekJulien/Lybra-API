from rest_framework import serializers

from apps.books.models import Book


class BookListLiteSerializer(serializers.ModelSerializer):
    available_copies_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Book
        fields = [
            'isbn', 'title', 'cover_url', 'available_copies_count'
        ]

