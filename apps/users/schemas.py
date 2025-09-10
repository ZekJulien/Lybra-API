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

get_by_id_schema = extend_schema(
    responses={
        200: UserSerializer,
        400: OpenApiResponse(description="Missing or invalid 'pk' parameter"),
        404: OpenApiResponse(description="User not found"),
        403: OpenApiResponse(description="Forbidden: Admin or employee access required"),
    },
    summary="Retrieve a user by ID",
    description="Endpoint to get a user by ID with 'pk' passed as a URL path parameter. Accessible only by authenticated employees and admins."
)

update_user_schema = extend_schema(
    request=UserSerializer,
    responses={
        200: UserSerializer,
        400: OpenApiResponse(description="Bad request, validation errors."),
        409: OpenApiResponse(description=UserMessage.USERNAME_TAKEN.value),
        404: OpenApiResponse(description=UserMessage.USER_NOT_FOUND.value),
    },
    summary="Update current user",
    description="Update fields of the authenticated user. Returns updated user data."
)

update_user_employee_schema = extend_schema(
    request=UserSerializer,
    responses={
        200: UserSerializer,
        400: OpenApiResponse(description="Bad request, validation errors or missing parameters."),
        404: OpenApiResponse(description=UserMessage.USER_NOT_FOUND.value),
        409: OpenApiResponse(description=UserMessage.USERNAME_TAKEN.value),
    },
    summary="Admin update user by ID",
    description="Allows an admin to update a user's information by specifying the user ID in the URL path. Supports partial updates."
)

user_schema = extend_schema_view(
    add = add_user_schema,
    get = get_user_schema,
    get_all_users = get_all_users_schema,
    update_user = update_user_schema,
    update_user_employee = update_user_employee_schema
)
