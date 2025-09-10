from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiResponse, extend_schema_view, OpenApiParameter

from apps.books.enums import BookError, BookSchema
from apps.books.serializers import BookSerializer, BookDetailSerializer

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
get_all_schema = extend_schema(
    parameters=[
        OpenApiParameter(name='title', type=OpenApiTypes.STR, location=OpenApiParameter.QUERY, required=False, description='Filter by book title'),
        OpenApiParameter(name='authors__name', type=OpenApiTypes.STR, location=OpenApiParameter.QUERY, required=False, description='Filter by author name'),
        OpenApiParameter(name='publication_date', type=OpenApiTypes.DATE, location=OpenApiParameter.QUERY, required=False, description='Filter by publication date'),
        OpenApiParameter(name='collection', type=OpenApiTypes.STR, location=OpenApiParameter.QUERY, required=False, description='Filter by collection ID'),
        OpenApiParameter(name='language', type=OpenApiTypes.STR, location=OpenApiParameter.QUERY, required=False, description='Filter by language code (e.g. "fr", "en")'),
        OpenApiParameter(name='pages', type=OpenApiTypes.INT, location=OpenApiParameter.QUERY, required=False, description='Filter by number of pages'),
        OpenApiParameter(name='genres__name', type=OpenApiTypes.STR, location=OpenApiParameter.QUERY, required=False, description='Filter by genre name'),
        OpenApiParameter(name='publishers__name', type=OpenApiTypes.STR, location=OpenApiParameter.QUERY, required=False, description='Filter by publisher name'),
        OpenApiParameter(name='themes__name', type=OpenApiTypes.STR, location=OpenApiParameter.QUERY, required=False, description='Filter by theme name'),
        OpenApiParameter(name='page', type=OpenApiTypes.INT, location=OpenApiParameter.QUERY, required=False, description='Page number for pagination'),
        OpenApiParameter(name='ordering', type=OpenApiTypes.STR, location=OpenApiParameter.QUERY, required=False, description='Ordering field (e.g. "title", "-publication_date")'),
    ],
    responses={
        200: OpenApiResponse(
            response=BookDetailSerializer(many=True),
            description="List of books with full related data, paginated."
        ),
        400: OpenApiResponse(description="Invalid query parameters."),
        403: OpenApiResponse(description="Forbidden.")
    },
    summary="Retrieve a paginated list of books",
    description="Returns a paginated list of books including authors, genres, publishers, themes, and collection details. Supports filtering and ordering via query parameters."
)

book_viewset_schema = extend_schema_view(
    add=add_book_schema,
    get_all=get_all_schema
)
