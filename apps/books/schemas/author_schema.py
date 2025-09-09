from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiResponse
from apps.books.serializers import AuthorSerializer

author_viewset_schema = extend_schema_view(
    list=extend_schema(
        summary="List all authors",
        description="Retrieve a list of all authors.",
        responses={200: AuthorSerializer(many=True)}
    ),
    retrieve=extend_schema(
        summary="Retrieve an author",
        description="Retrieve details of a specific author by ID.",
        responses={200: AuthorSerializer()}
    ),
    create=extend_schema(
        summary="Create a new author",
        description="Create a new author with required fields.",
        responses={201: AuthorSerializer(), 400: OpenApiResponse(description="Bad Request")}
    ),
    update=extend_schema(
        summary="Update an author",
        description="Update all fields of an existing author.",
        responses={200: AuthorSerializer(), 400: OpenApiResponse(description="Bad Request")}
    ),
    partial_update=extend_schema(
        summary="Partially update an author",
        description="Update some fields of an existing author.",
        responses={200: AuthorSerializer(), 400: OpenApiResponse(description="Bad Request")}
    ),
    destroy=extend_schema(
        summary="Delete an author",
        description="Delete an existing author by ID.",
        responses={204: OpenApiResponse(description="No Content")}
    )
)
