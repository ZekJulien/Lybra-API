from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiResponse, extend_schema_view, OpenApiParameter

from apps.books.enums import BookError, BookSchema
from apps.books.serializers import BookSerializer, BookDetailSerializer, BookListSerializer, BookListLiteSerializer

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
        OpenApiParameter(name='expand', type=OpenApiTypes.STR, location=OpenApiParameter.QUERY, required=False, description="Comma-separated: authors,genres,publishers,themes,collection"),
    ],
    responses={
        200: OpenApiResponse(
            response=BookListLiteSerializer(many=True),
            description="List of books. If 'expand' provided, relations are included."
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

update_book_schema = extend_schema(
    request=BookSerializer,
    responses={
        200: BookDetailSerializer,
        400: OpenApiResponse(description=BookError.INVALID_DATA.value),
        404: OpenApiResponse(description=BookError.BOOK_NOT_FOUND.value),
    },
    summary="Update an existing book",
    description="Updates an existing book identified by ISBN with the provided data.",
)

delete_book_schema = extend_schema(
    responses={
        204: OpenApiResponse(description="Book deleted successfully"),
        404: OpenApiResponse(description=BookError.BOOK_NOT_FOUND.value),
    },
    summary="Delete a book by ISBN",
    description="Deletes the book identified by the given ISBN. Returns 204 No Content on success.",
)

book_viewset_schema = extend_schema_view(
    add=add_book_schema,
    get_all=get_all_schema,
    get=get_by_isbn_schema,
    update_book=update_book_schema,
    delete_book=delete_book_schema,
)


