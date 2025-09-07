from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiResponse
from rest_framework import serializers
from apps.auths.serializers import AuthSerializer, UpdatePasswordSerializers, LogoutRequestSerializer, \
    CustomTokenRefreshSerializer, CustomTokenObtainPairSerializer


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
    request=CustomTokenObtainPairSerializer,
    responses=CustomTokenObtainPairSerializer,
    summary="Login",
    description="Obtain a JWT token with email and password"
)

refresh_schema = extend_schema(
    request=CustomTokenRefreshSerializer,
    responses=CustomTokenRefreshSerializer,
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

update_password_schema = extend_schema(
    request=UpdatePasswordSerializers,
    responses={
        200: OpenApiResponse(description="Your password has been successfully updated.")
    },
    summary="Update Password",
    description="Allows users to update their password."
)



auth_schema = extend_schema_view(
    token=token_schema,
    token_refresh=refresh_schema,
    init_admin=init_admin_schema,
    create_user=create_user_schema,
    create_employee=create_employee_schema,
    get_me=get_me_schema,
    logout=logout_schema,
    update_password=update_password_schema,
)


