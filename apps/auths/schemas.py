from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiResponse
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from auths.serializers import AuthSerializer
from auths.serializers.logout_serializer import LogoutRequestSerializer


class TokenResponseSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()

init_admin_schema = extend_schema(
    request=AuthSerializer,
    responses={
        200: OpenApiResponse(description="Account created successfully")
    },
    summary="Initialize the first administrator"
)

create_user_schema = extend_schema(
    request=AuthSerializer,
    responses={
        200: OpenApiResponse(description="Account created successfully")
    },
    summary="Create a new user"
)

create_employee_schema = extend_schema(
    request=AuthSerializer,
    responses={
        200: OpenApiResponse(description="Account created successfully")
    },
    summary="Create a new employee"
)

token_schema = extend_schema(
    request=TokenObtainPairSerializer,
    responses=TokenResponseSerializer,
    summary="Login",
    description="Obtain a JWT token with email and password"
)

refresh_schema = extend_schema(
    request=TokenRefreshSerializer,
    responses=TokenResponseSerializer,
    summary="Refresh",
    description="Refresh the JWT token"
)

get_me_schema = extend_schema(
    responses=AuthSerializer,
    summary="Get current user info",
    description="Get email, last_login and date_joined about user.",
)

logout_schema = extend_schema(
    request=LogoutRequestSerializer,
    responses={
        205: OpenApiResponse(
            description=(
                "Logout successful — no content returned. "
                "Client should reset view.\n\n"
                "**Headers:**\n"
                "`Clear-Site-Data: \"cache, cookies\"` — Indicates which client-side data should be cleared."
            )
        )
    },
    summary="Logout",
    description="Invalidate and blacklist the refresh token. Returns 205 to signal client-side reset."
)



auth_schema = extend_schema_view(
    token=token_schema,
    token_refresh=refresh_schema,
    init_admin=init_admin_schema,
    create_user=create_user_schema,
    create_employee=create_employee_schema,
    get_me=get_me_schema,
    logout=logout_schema,
)


