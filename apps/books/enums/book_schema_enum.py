from enum import Enum

class BookSchema(Enum):
    ADD_BOOK_SUMMARY = "Create a new book"
    ADD_BOOK_DESCRIPTION = "Creates a new book from the provided data. All relations are checked in the database."