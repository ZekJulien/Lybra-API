from rest_framework import serializers

from apps.books.models import Book
from apps.books.serializers import AuthorSerializer, CollectionSerializer, GenreSerializer, PublisherSerializer, \
    ThemeSerializer


class BookDetailSerializer(serializers.ModelSerializer):
    """Serializer for detailed representation of the Book model."""
    authors = AuthorSerializer(many=True, read_only=True)
    collection = CollectionSerializer(read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    publishers = PublisherSerializer(many=True, read_only=True)
    themes = ThemeSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = [
            'isbn', 'title', 'summary', 'language', 'publication_date',
            'cover_url', 'pages', 'collection', 'authors', 'genres',
            'publishers', 'themes'
        ]