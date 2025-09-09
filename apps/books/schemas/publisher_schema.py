from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiResponse
from apps.books.serializers import PublisherSerializer

publisher_viewset_schema = extend_schema_view(
    list=extend_schema(
        summary="List all publishers",
        description="Retrieve a list of all publishers.",
        responses={200: PublisherSerializer(many=True)}
    ),
    retrieve=extend_schema(
        summary="Retrieve an publisher",
        description="Retrieve details of a specific publisher by ID.",
        responses={200: PublisherSerializer()}
    ),
    create=extend_schema(
        summary="Create a new publisher",
        description="Create a new publisher with required fields.",
        responses={201: PublisherSerializer(), 400: OpenApiResponse(description="Bad Request")}
    ),
    update=extend_schema(
        summary="Update an publisher",
        description="Update all fields of an existing publisher.",
        responses={200: PublisherSerializer(), 400: OpenApiResponse(description="Bad Request")}
    ),
    partial_update=extend_schema(
        summary="Partially update an publisher",
        description="Update some fields of an existing publisher.",
        responses={200: PublisherSerializer(), 400: OpenApiResponse(description="Bad Request")}
    ),
    destroy=extend_schema(
        summary="Delete an publisher",
        description="Delete an existing publisher by ID.",
        responses={204: OpenApiResponse(description="No Content")}
    )
)