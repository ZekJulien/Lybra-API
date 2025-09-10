from drf_spectacular.utils import extend_schema, OpenApiResponse, extend_schema_view
from apps.books.serializers import BookCopySerializer

add_bookcopy_schema = extend_schema(
    request=BookCopySerializer,
    responses={
        201: BookCopySerializer,
        400: OpenApiResponse(description="Invalid data provided"),
    },
    summary="Create a new book copy",
    description="Creates a new physical copy of an existing book identified by its ISBN.",
)

get_all_bookcopies_schema = extend_schema(
    responses={
        200: BookCopySerializer(many=True),
        400: OpenApiResponse(description="Invalid query parameters"),
    },
    summary="Retrieve all book copies",
    description="Returns a list of all book copies with statuses and locations.",
)

update_bookcopy_schema = extend_schema(
    request=BookCopySerializer,
    responses={
        200: BookCopySerializer,
        400: OpenApiResponse(description="Invalid data provided"),
        404: OpenApiResponse(description="Book copy not found"),
    },
    summary="Update a book copy",
    description="Update details of a physical book copy by its ISBN.",
)

delete_bookcopy_schema = extend_schema(
    responses={
        204: OpenApiResponse(description="Book copy deleted successfully"),
        404: OpenApiResponse(description="Book copy not found"),
    },
    summary="Delete a book copy",
    description="Deletes a physical book copy identified by its ISBN.",
)

bookcopy_viewset_schema = extend_schema_view(
    create=add_bookcopy_schema,
    list=get_all_bookcopies_schema,
    update=update_bookcopy_schema,
    partial_update=update_bookcopy_schema,
    destroy=delete_bookcopy_schema,
)
