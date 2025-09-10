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
        OpenApiParameter(name='title', type=OpenApiTypes.STR, location=OpenApiParameter.QUERY, required=False, description=BookSchema.PARAM_TITLE_DESC.value),
        OpenApiParameter(name='authors__name', type=OpenApiTypes.STR, location=OpenApiParameter.QUERY, required=False, description=BookSchema.PARAM_AUTHOR_NAME_DESC.value),
        OpenApiParameter(name='publication_date', type=OpenApiTypes.DATE, location=OpenApiParameter.QUERY, required=False, description=BookSchema.PARAM_PUBLICATION_DATE_DESC.value),
        OpenApiParameter(name='collection', type=OpenApiTypes.STR, location=OpenApiParameter.QUERY, required=False, description=BookSchema.PARAM_COLLECTION_DESC.value),
        OpenApiParameter(name='language', type=OpenApiTypes.STR, location=OpenApiParameter.QUERY, required=False, description=BookSchema.PARAM_LANGUAGE_DESC.value),
        OpenApiParameter(name='pages', type=OpenApiTypes.INT, location=OpenApiParameter.QUERY, required=False, description=BookSchema.PARAM_PAGES_DESC.value),
        OpenApiParameter(name='genres__name', type=OpenApiTypes.STR, location=OpenApiParameter.QUERY, required=False, description=BookSchema.PARAM_GENRE_NAME_DESC.value),
        OpenApiParameter(name='publishers__name', type=OpenApiTypes.STR, location=OpenApiParameter.QUERY, required=False, description=BookSchema.PARAM_PUBLISHER_NAME_DESC.value),
        OpenApiParameter(name='themes__name', type=OpenApiTypes.STR, location=OpenApiParameter.QUERY, required=False, description=BookSchema.PARAM_THEME_NAME_DESC.value),
        OpenApiParameter(name='page', type=OpenApiTypes.INT, location=OpenApiParameter.QUERY, required=False, description=BookSchema.PARAM_PAGE_DESC.value),
        OpenApiParameter(name='ordering', type=OpenApiTypes.STR, location=OpenApiParameter.QUERY, required=False, description=BookSchema.PARAM_ORDERING_DESC.value),
    ],
    responses={
        200: OpenApiResponse(
            response=BookDetailSerializer(many=True),
            description="List of books with full related data, paginated."
        ),
        400: OpenApiResponse(description=BookError.INVALID_DATA.value),
        403: OpenApiResponse(description="Forbidden."),
    },
    summary=BookSchema.GET_ALL_SUMMARY.value,
    description=BookSchema.GET_ALL_DESCRIPTION.value,
)

get_by_isbn_schema = extend_schema(
    parameters=[
        OpenApiParameter(
            name='isbn',
            type=OpenApiTypes.STR,
            location=OpenApiParameter.PATH,
            required=True,
            description=BookSchema.PARAM_ISBN_DESC.value,
        ),
    ],
    responses={
        200: OpenApiResponse(response=BookDetailSerializer, description="Book details retrieved successfully"),
        400: OpenApiResponse(description=BookError.INVALID_ISBN_FORMAT.value),
        404: OpenApiResponse(description=BookError.BOOK_NOT_FOUND.value),
    },
    summary=BookSchema.GET_BY_ID_SUMMARY.value,
    description=BookSchema.GET_BY_ID_DESCRIPTION.value,
)

book_viewset_schema = extend_schema_view(
    add=add_book_schema,
    get_all=get_all_schema,
    get_by_id=get_by_isbn_schema,
)
