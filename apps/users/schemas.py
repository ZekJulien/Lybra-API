from drf_spectacular.utils import extend_schema, OpenApiResponse, extend_schema_view

from apps.users.enums import UserMessage
from apps.users.serializers import UserSerializer

add_user_schema = extend_schema(
    request=UserSerializer,
    responses=UserSerializer,
    summary="Add a new user",
    description="Creates a new user with the provided data."
)

user_schema = extend_schema_view(
    add = add_user_schema
)
