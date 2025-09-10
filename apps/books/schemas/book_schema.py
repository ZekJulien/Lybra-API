from drf_spectacular.utils import extend_schema, OpenApiResponse, extend_schema_view

from apps.books.enums import BookError, BookSchema
from apps.books.serializers import BookSerializer

add_book_schema = extend_schema(
    request=BookSerializer,
    responses={
        201: BookSerializer,
        400: OpenApiResponse(description=BookError.INVALID_DATA.value),
        404: OpenApiResponse(description=BookError.COLLECTION_NOT_FOUND.value),
        409: OpenApiResponse(description=BookError.ALREADY_EXIST_BOOK.value),
    },
    summary=BookSchema.ADD_BOOK_SUMMARY.value,
    description=BookSchema.ADD_BOOK_DESCRIPTION.value,
)

book_viewset_schema = extend_schema_view(
    add=add_book_schema,
)
