from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiResponse
from apps.books.serializers import ThemeSerializer

theme_viewset_schema = extend_schema_view(
    list=extend_schema(
        summary="List all themes",
        description="Retrieve a list of all themes.",
        responses={200: ThemeSerializer(many=True)}
    ),
    retrieve=extend_schema(
        summary="Retrieve a theme",
        description="Retrieve details of a specific theme by ID.",
        responses={200: ThemeSerializer()}
    ),
    create=extend_schema(
        summary="Create a new theme",
        description="Create a new theme with required fields.",
        responses={201: ThemeSerializer(), 400: OpenApiResponse(description="Bad Request")}
    ),
    update=extend_schema(
        summary="Update a theme",
        description="Update all fields of an existing theme.",
        responses={200: ThemeSerializer(), 400: OpenApiResponse(description="Bad Request")}
    ),
    partial_update=extend_schema(
        summary="Partially update a theme",
        description="Update some fields of an existing theme.",
        responses={200: ThemeSerializer(), 400: OpenApiResponse(description="Bad Request")}
    ),
    destroy=extend_schema(
        summary="Delete a theme",
        description="Delete an existing theme by ID.",
        responses={204: OpenApiResponse(description="No Content")}
    )
)
