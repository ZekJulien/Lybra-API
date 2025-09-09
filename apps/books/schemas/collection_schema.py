from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiResponse
from apps.books.serializers import CollectionSerializer

collection_viewset_schema = extend_schema_view(
    list=extend_schema(
        summary="List all collections",
        description="Retrieve a list of all collections.",
        responses={200: CollectionSerializer(many=True)}
    ),
    retrieve=extend_schema(
        summary="Retrieve a collection",
        description="Retrieve details of a specific collection by ID.",
        responses={200: CollectionSerializer()}
    ),
    create=extend_schema(
        summary="Create a new collection",
        description="Create a new collection with required fields.",
        responses={201: CollectionSerializer(), 400: OpenApiResponse(description="Bad Request")}
    ),
    update=extend_schema(
        summary="Update a collection",
        description="Update all fields of an existing collection.",
        responses={200: CollectionSerializer(), 400: OpenApiResponse(description="Bad Request")}
    ),
    partial_update=extend_schema(
        summary="Partially update a collection",
        description="Update some fields of an existing collection.",
        responses={200: CollectionSerializer(), 400: OpenApiResponse(description="Bad Request")}
    ),
    destroy=extend_schema(
        summary="Delete a collection",
        description="Delete an existing collection by ID.",
        responses={204: OpenApiResponse(description="No Content")}
    )
)

