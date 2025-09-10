import pytest
from uuid import uuid4
from django.core.exceptions import ValidationError
from apps.books.models import Book, Author, Genre, Publisher, Theme, Collection
from apps.books.services import BookService
from apps.books.enums import BookError

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

@pytest.mark.django_db
def test_get_all_returns_books_with_relations():
    collection = Collection.objects.create(id=uuid4(), name='Test Collection')

    author = Author.objects.create(id=uuid4(), name='Author 1')
    genre = Genre.objects.create(id=uuid4(), name='Genre 1')
    publisher = Publisher.objects.create(id=uuid4(), name='Publisher 1')
    theme = Theme.objects.create(id=uuid4(), name='Theme 1')

    book = Book.objects.create(
        isbn='1234567890123',
        title='Test Book',
        summary='Summary',
        language='EN',
        publication_date='2025-01-01',
        pages=100,
        collection=collection
    )
    book.authors.add(author)
    book.genres.add(genre)
    book.publishers.add(publisher)
    book.themes.add(theme)

    queryset = BookService.get_all()
    # Le queryset doit contenir le livre créé
    assert book in queryset

    # Accès aux relations sans requêtes supplémentaires (le test N+1 ici serait plus avancé)
    result_book = queryset.get(isbn='1234567890123')
    assert list(result_book.authors.all()) == [author]
    assert list(result_book.genres.all()) == [genre]
    assert list(result_book.publishers.all()) == [publisher]
    assert list(result_book.themes.all()) == [theme]
    assert result_book.collection == collection

@pytest.mark.django_db
def test_update_book_success():
    collection = Collection.objects.create(name="Collection Test")
    author = Author.objects.create(name="Auteur Test")
    genre = Genre.objects.create(name="Genre Test")
    publisher = Publisher.objects.create(name="Publisher Test")
    theme = Theme.objects.create(name="Theme Test")

    book = Book.objects.create(
        isbn="1234567890123",
        title="Old Title",
        summary="Old Summary",
        language="fr",
        publication_date="2020-01-01",
        pages=100,
        collection=collection,
    )
    book.authors.add(author)
    book.genres.add(genre)
    book.publishers.add(publisher)
    book.themes.add(theme)

    new_collection = Collection.objects.create(name="Nouvelle Collection")
    new_author = Author.objects.create(name="Nouvel Auteur")
    new_genre = Genre.objects.create(name="Nouveau Genre")
    new_publisher = Publisher.objects.create(name="Nouveau Publisher")
    new_theme = Theme.objects.create(name="Nouveau Theme")

    data = {
        "isbn": book.isbn,
        "title": "New Title",
        "summary": "New Summary",
        "language": "en",
        "publication_date": "2025-01-01",
        "cover_url": "https://example.com/cover.jpg",
        "pages": 200,
        "collection": str(new_collection.pk),
        "authors": [str(new_author.pk)],
        "genres": [str(new_genre.pk)],
        "publishers": [str(new_publisher.pk)],
        "themes": [str(new_theme.pk)],
    }

    updated_book = BookService.update(data)

    assert updated_book.pk == book.pk
    assert updated_book.title == "New Title"
    assert updated_book.summary == "New Summary"
    assert updated_book.language == "en"
    assert str(updated_book.collection.pk) == str(new_collection.pk)
    assert updated_book.pages == 200
    assert updated_book.cover_url == "https://example.com/cover.jpg"
    assert set(a.pk for a in updated_book.authors.all()) == {new_author.pk}
    assert set(g.pk for g in updated_book.genres.all()) == {new_genre.pk}
    assert set(p.pk for p in updated_book.publishers.all()) == {new_publisher.pk}
    assert set(t.pk for t in updated_book.themes.all()) == {new_theme.pk}

@pytest.mark.django_db
def test_update_book_not_found():
    data = {"isbn": "nonexistentisbn", "collection": "some-uuid"}
    with pytest.raises(ValidationError) as excinfo:
        BookService.update(data)
    assert BookError.BOOK_NOT_FOUND.value in str(excinfo.value)

@pytest.mark.django_db
def test_delete_book_success():
    collection = Collection.objects.create(name="Test Collection")
    book = Book.objects.create(
        isbn="1234567890123",
        title="Titre",
        summary="Résumé",
        language="fr",
        publication_date="2020-01-01",
        pages=100,
        collection=collection,
    )
    BookService.delete(book.isbn)

    assert Book.objects.filter(pk=book.pk).count() == 0

@pytest.mark.django_db
def test_delete_book_not_found():
    with pytest.raises(ValidationError) as excinfo:
        BookService.delete("nonexistentisbn")
    assert BookError.BOOK_NOT_FOUND.value in str(excinfo.value)