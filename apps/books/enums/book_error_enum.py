from enum import Enum

class BookError(Enum):
    COLLECTION_NOT_FOUND = "Collection not found in the database."
    AUTHORS_NOT_FOUND = "One or more authors are missing."
    GENRES_NOT_FOUND = "One or more genres are missing."
    PUBLISHERS_NOT_FOUND = "One or more publishers are missing."
    THEMES_NOT_FOUND = "One or more themes are missing."
    INVALID_ISBN = "The provided ISBN number is invalid."
    INVALID_LANGUAGE = "The language code is invalid, must be two letters (e.g., 'FR', 'EN')."
    REQUIRED_FIELD_MISSING = "A required field is missing."
    INVALID_DATE_FORMAT = "The date format is invalid, must be YYYY-MM-DD."
    INVALID_INTEGER_VALUE = "Invalid integer value."
    GENERIC_VALIDATION_ERROR = "Unknown validation error."
    INVALID_DATA = "Invalid or missing data."
    ALREADY_EXIST_BOOK = "Book already exists."