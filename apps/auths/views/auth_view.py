from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from auths.schemas import auth_schema
from auths.serializers import AuthSerializer, UpdatePasswordSerializers, CustomTokenRefreshSerializer, \
    CustomTokenObtainPairSerializer
from auths.services import AuthService
from auths.permissions import IsFirstUser, IsAdminUser, IsAuthenticatedWithChecks


@auth_schema
class AuthView(ViewSet):
    """ViewSet for user-related operations including registration, admin initialization, and employee creation."""

    @action(detail=False, methods=['post'], url_path='init', permission_classes=[IsFirstUser])
    def init_admin(self, request):
        """Creates the first admin user if no users exist."""
        serializer = AuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        AuthService.add_admin(serializer.validated_data)
        return Response({ "message": "Account created successfully" }, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], url_path='register')
    def create_user(self, request):
        """Creates a regular user."""
        serializer = AuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        AuthService.add(serializer.validated_data)
        return Response({ "message": "Account created successfully" }, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], url_path='employee', permission_classes=[IsAdminUser])
    def create_employee(self, request):
        """Creates an employee user. Only accessible by admin users."""
        serializer = AuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        AuthService.add_employee(serializer.validated_data)
        return Response({ "message": "Account created successfully" }, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], url_path='token')
    def token(self, request):
        """Generates JWT tokens for user authentication and update last_login."""
        serializer = CustomTokenObtainPairSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        AuthService.update_last_login(serializer.user.id)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], url_path='token/refresh')
    def token_refresh(self, request):
        """Generates new access tokens with JWT."""
        serializer = CustomTokenRefreshSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='me', permission_classes=[IsAuthenticatedWithChecks])
    def get_me(self, request):
        """Retrieves the authenticated user's details."""
        user = AuthService.me(request.user.id)
        serializer = AuthSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"], url_path="logout", permission_classes=[IsAuthenticatedWithChecks])
    def logout(self, request):
        """Logs out the user by blacklisting the refresh token."""
        refresh_token = request.data.get("refresh")
        if not refresh_token:
            return Response({"detail": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)
        AuthService.blacklist_refresh_token(refresh_token)
        return Response({"detail": "Logout successfully."}, status=status.HTTP_205_RESET_CONTENT)

    @action(detail=False, methods=["put"], url_path="password", permission_classes=[IsAuthenticatedWithChecks])
    def update_password(self, request):
        """Updates the authenticated user's password."""
        serializer = UpdatePasswordSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        AuthService.update_password(request.user.id, serializer.validated_data["old_password"],serializer.validated_data["new_password"])
        return Response({"detail": "Your password has been successfully updated."}, status=status.HTTP_200_OK)
