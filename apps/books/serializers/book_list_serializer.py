from rest_framework import serializers

from apps.books.models import Book
from apps.books.serializers.author_serializer import AuthorSerializer
from apps.books.serializers.collection_serializer import CollectionSerializer
from apps.books.serializers.genre_serializer import GenreSerializer
from apps.books.serializers.publisher_serializer import PublisherSerializer
from apps.books.serializers.theme_serializer import ThemeSerializer


class BookListSerializer(serializers.ModelSerializer):
    available_copies_count = serializers.IntegerField(read_only=True)
    authors = AuthorSerializer(many=True, read_only=True)
    collection = CollectionSerializer(read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    publishers = PublisherSerializer(many=True, read_only=True)
    themes = ThemeSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = [
            'isbn', 'title', 'cover_url', 'summary', 'language', 'publication_date', 'pages',
            'collection', 'authors', 'genres', 'publishers', 'themes',
            'available_copies_count'
        ]

    def get_fields(self):
        fields = super().get_fields()
        # Base fields always included when using this serializer
        base_fields = {
            'isbn', 'title', 'cover_url', 'summary', 'language', 'publication_date', 'pages',
            'available_copies_count'
        }
        expands = self.context.get('expands', set()) or set()
        allowed_expands = {'authors', 'genres', 'publishers', 'themes', 'collection'}

        requested = base_fields.union(expands.intersection(allowed_expands))

        # Drop any fields not requested
        for field_name in list(fields.keys()):
            if field_name not in requested:
                fields.pop(field_name)
        return fields

