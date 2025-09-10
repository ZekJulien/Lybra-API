from django.core.exceptions import ValidationError
from apps.books.models import Book, Author, Genre, Publisher, Theme, Collection
from django.db import transaction

from apps.books.enums import BookError
from apps.books.types import BookPayload


class BookService:

    @staticmethod
    def _get_and_validate_related_objects(data):
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

        return collection, authors, genres, publishers, themes


    @staticmethod
    @transaction.atomic
    def add(data: BookPayload):
        """Service method to add a new book to the database."""
        existing_book = Book.objects.filter(pk=data['isbn']).first()
        if existing_book:
            raise ValidationError(BookError.ALREADY_EXIST_BOOK.value)

        collection, authors, genres, publishers, themes = BookService._get_and_validate_related_objects(data)

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

    @staticmethod
    def get_by_isbn(isbn) -> Book:
        """Service method to retrieve a single book by ISBN."""
        book = Book.objects.filter(isbn=isbn).first()
        if not book:
            raise ValidationError(BookError.BOOK_NOT_FOUND.value)
        return book

    @staticmethod
    @transaction.atomic
    def update(data: BookPayload) -> Book:
        """Service method to update an existing book by ISBN."""
        book = Book.objects.filter(isbn=data['isbn']).first()
        if not book:
            raise ValidationError(BookError.BOOK_NOT_FOUND.value)

        collection, authors, genres, publishers, themes = BookService._get_and_validate_related_objects(data)

        book.title = data['title']
        book.summary = data['summary']
        book.language = data['language']
        book.publication_date = data['publication_date']
        book.cover_url = data.get('cover_url')
        book.pages = data['pages']
        book.collection = collection

        book.save()

        if authors:
            book.authors.set(authors)
        else:
            book.authors.clear()

        if genres:
            book.genres.set(genres)
        else:
            book.genres.clear()

        if publishers:
            book.publishers.set(publishers)
        else:
            book.publishers.clear()

        if themes:
            book.themes.set(themes)
        else:
            book.themes.clear()

        return book