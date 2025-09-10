import pytest
from uuid import uuid4
from django.core.exceptions import ValidationError
from apps.books.models import Book, Author, Genre, Publisher, Theme, Collection
from apps.books.services import BookService
from apps.books.enums.book_error_enum import BookError

@pytest.mark.django_db
def test_book_create_minimal():
    collection = Collection.objects.create(id=uuid4(), name='Test Coll')
    payload = {
        'isbn': '1234567890123',
        'title': 'My Book',
        'summary': 'Résumé',
        'language': 'FR',
        'publication_date': '2025-09-09',
        'cover_url': None,
        'pages': 111,
        'collection': str(collection.id),
        'authors': [],
        'genres': [],
        'publishers': [],
        'themes': [],
    }
    book = BookService.add(payload)
    assert Book.objects.filter(isbn=payload['isbn']).exists()
    assert book.authors.count() == 0
    assert book.genres.count() == 0
    assert book.publishers.count() == 0
    assert book.themes.count() == 0

@pytest.mark.django_db
def test_book_create_with_relations():
    collection = Collection.objects.create(id=uuid4(), name='Test Coll')
    author1 = Author.objects.create(id=uuid4(), name='Author1')
    genre1 = Genre.objects.create(id=uuid4(), name='Genre1')
    publisher1 = Publisher.objects.create(id=uuid4(), name='Publisher1')
    theme1 = Theme.objects.create(id=uuid4(), name='Theme1')
    payload = {
        'isbn': '9876543210987',
        'title': 'Other Book',
        'summary': 'Résumé B',
        'language': 'EN',
        'publication_date': '2025-08-03',
        'cover_url': '',
        'pages': 222,
        'collection': str(collection.id),
        'authors': [str(author1.id)],
        'genres': [str(genre1.id)],
        'publishers': [str(publisher1.id)],
        'themes': [str(theme1.id)],
    }
    book = BookService.add(payload)
    assert list(book.authors.all()) == [author1]
    assert list(book.genres.all()) == [genre1]
    assert list(book.publishers.all()) == [publisher1]
    assert list(book.themes.all()) == [theme1]

@pytest.mark.django_db
def test_book_create_error_collection():
    payload = {
        'isbn': '0000000000001',
        'title': 'Err',
        'summary': 'Résumé',
        'language': 'FR',
        'publication_date': '2025-09-09',
        'cover_url': None,
        'pages': 100,
        'collection': str(uuid4()),
        'authors': [],
        'genres': [],
        'publishers': [],
        'themes': [],
    }
    with pytest.raises(ValidationError) as excinfo:
        BookService.add(payload)
    assert BookError.COLLECTION_NOT_FOUND.value in str(excinfo.value)

@pytest.mark.django_db
def test_book_create_error_authors():
    collection = Collection.objects.create(id=uuid4(), name='Test Coll')
    payload = {
        'isbn': '0000000000002',
        'title': 'ErrAuth',
        'summary': 'Résumé',
        'language': 'FR',
        'publication_date': '2025-09-09',
        'cover_url': None,
        'pages': 101,
        'collection': str(collection.id),
        'authors': [str(uuid4())],
        'genres': [],
        'publishers': [],
        'themes': [],
    }
    with pytest.raises(ValidationError) as excinfo:
        BookService.add(payload)
    assert BookError.AUTHORS_NOT_FOUND.value in str(excinfo.value)
