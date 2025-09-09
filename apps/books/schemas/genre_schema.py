from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiResponse
from apps.books.serializers import GenreSerializer

genre_viewset_schema = extend_schema_view(
    list=extend_schema(
        summary="List all genres",
        description="Retrieve a list of all genres.",
        responses={200: GenreSerializer(many=True)}
    ),
    retrieve=extend_schema(
        summary="Retrieve a genre",
        description="Retrieve details of a specific genre by ID.",
        responses={200: GenreSerializer()}
    ),
    create=extend_schema(
        summary="Create a new genre",
        description="Create a new genre with required fields.",
        responses={201: GenreSerializer(), 400: OpenApiResponse(description="Bad Request")}
    ),
    update=extend_schema(
        summary="Update a genre",
        description="Update all fields of an existing genre.",
        responses={200: GenreSerializer(), 400: OpenApiResponse(description="Bad Request")}
    ),
    partial_update=extend_schema(
        summary="Partially update a genre",
        description="Update some fields of an existing genre.",
        responses={200: GenreSerializer(), 400: OpenApiResponse(description="Bad Request")}
    ),
    destroy=extend_schema(
        summary="Delete a genre",
        description="Delete an existing genre by ID.",
        responses={204: OpenApiResponse(description="No Content")}
    )
)
