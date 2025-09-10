from enum import Enum

class BookSchema(Enum):
    ADD_BOOK_SUMMARY = "Create a new book"
    GET_ALL_SUMMARY = "Retrieve a paginated list of books"
    GET_BY_ID_SUMMARY = "Retrieve a single book by ISBN"

    ADD_BOOK_DESCRIPTION = "Creates a new book from the provided data. All relations are checked in the database."
    GET_ALL_DESCRIPTION = "Returns a paginated list of books including authors, genres, publishers, themes, and collection details. Supports filtering and ordering via query parameters."
    GET_BY_ID_DESCRIPTION = "Returns the detail of a book identified by its ISBN."

    PARAM_TITLE_DESC = "Filter by book title"
    PARAM_AUTHOR_NAME_DESC = "Filter by author name"
    PARAM_PUBLICATION_DATE_DESC = "Filter by publication date"
    PARAM_COLLECTION_DESC = "Filter by collection ID"
    PARAM_LANGUAGE_DESC = 'Filter by language code (e.g. "fr", "en")'
    PARAM_PAGES_DESC = "Filter by number of pages"
    PARAM_GENRE_NAME_DESC = "Filter by genre name"
    PARAM_PUBLISHER_NAME_DESC = "Filter by publisher name"
    PARAM_THEME_NAME_DESC = "Filter by theme name"
    PARAM_PAGE_DESC = "Page number for pagination"
    PARAM_ORDERING_DESC = 'Ordering field (e.g. "title", "-publication_date")'
    PARAM_ISBN_DESC = "ISBN of the book to retrieve (13 digits, with or without hyphens)"
