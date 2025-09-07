from drf_spectacular.utils import extend_schema, OpenApiResponse, extend_schema_view

from apps.users.enums import UserMessage
from apps.users.serializers import UserSerializer

add_user_schema = extend_schema(
    request=UserSerializer,
    responses=UserSerializer,
    summary="Add a new user",
    description="Creates a new user with the provided data."
)

get_user_schema = extend_schema(
    responses={
        200: UserSerializer,
        404: OpenApiResponse(description=UserMessage.USER_NOT_FOUND.value)
    },
    summary="Retrieve a user by ID",
    description="Returns user details for a given user UUID. Returns 404 if not found."
)

get_all_users_schema = extend_schema(
    responses={
        200: UserSerializer(many=True),
        403: OpenApiResponse(description="Forbidden: Admin access required.")
    },
    summary="Retrieve all users",
    description="Retrieve a list of all users. Admin permission required."
)

user_schema = extend_schema_view(
    add = add_user_schema,
    get = get_user_schema,
    get_all_users = get_all_users_schema,
)
