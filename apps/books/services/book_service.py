from django.core.exceptions import ValidationError
from apps.books.models import Book, Author, Genre, Publisher, Theme, Collection
from django.db import transaction

from apps.books.enums import BookError
from apps.books.types import BookPayload


class BookService:

    @staticmethod
    @transaction.atomic
    def add(data: BookPayload):
        """Service method to add a new book to the database."""
        existing_book = Book.objects.filter(pk=data['isbn']).first()
        if existing_book:
            raise ValidationError(BookError.ALREADY_EXIST_BOOK.value)


        collection = Collection.objects.filter(pk=data['collection']).first()
        if not collection:
            raise ValidationError(BookError.COLLECTION_NOT_FOUND.value)

        authors_ids = data.get('authors', [])
        if authors_ids:
            authors = Author.objects.filter(id__in=authors_ids)
            if authors.count() != len(authors_ids):
                raise ValidationError(BookError.AUTHORS_NOT_FOUND.value)
        else:
            authors = []

        genres_ids = data.get('genres', [])
        if genres_ids:
            genres = Genre.objects.filter(id__in=genres_ids)
            if genres.count() != len(genres_ids):
                raise ValidationError(BookError.GENRES_NOT_FOUND.value)
        else:
            genres = []

        publishers_ids = data.get('publishers', [])
        if publishers_ids:
            publishers = Publisher.objects.filter(id__in=publishers_ids)
            if publishers.count() != len(publishers_ids):
                raise ValidationError(BookError.PUBLISHERS_NOT_FOUND.value)
        else:
            publishers = []

        themes_ids = data.get('themes', [])
        if themes_ids:
            themes = Theme.objects.filter(id__in=themes_ids)
            if themes.count() != len(themes_ids):
                raise ValidationError(BookError.THEMES_NOT_FOUND.value)
        else:
            themes = []

        book = Book.objects.create(
            isbn=data['isbn'],
            title=data['title'],
            summary=data['summary'],
            language=data['language'],
            publication_date=data['publication_date'],
            cover_url=data.get('cover_url'),
            pages=data['pages'],
            collection=collection,
        )

        if authors:
            book.authors.set(authors)
        if genres:
            book.genres.set(genres)
        if publishers:
            book.publishers.set(publishers)
        if themes:
            book.themes.set(themes)

        return book

    @staticmethod
    def get_all():
        """Service method to retrieve all books."""
        return Book.objects.select_related('collection').prefetch_related(
            'authors', 'genres', 'publishers', 'themes'
        ).all()
