from rest_framework import serializers

from apps.books.models import Book
from apps.books.serializers.author_serializer import AuthorSerializer
from apps.books.serializers.collection_serializer import CollectionSerializer
from apps.books.serializers.genre_serializer import GenreSerializer
from apps.books.serializers.publisher_serializer import PublisherSerializer
from apps.books.serializers.theme_serializer import ThemeSerializer
from apps.books.serializers.book_copy_serializer import BookCopySerializer


class BookDetailSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    collection = CollectionSerializer(read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    publishers = PublisherSerializer(many=True, read_only=True)
    themes = ThemeSerializer(many=True, read_only=True)
    copies = BookCopySerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = [
            'isbn', 'title', 'summary', 'language', 'publication_date',
            'cover_url', 'pages', 'collection', 'authors', 'genres',
            'publishers', 'themes', 'copies'
        ]