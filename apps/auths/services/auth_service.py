from uuid import UUID

from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.timezone import now

from auths.models import Auth
from shared.exceptions import AuthServiceError


class AuthService:
    """Service layer for user creation and management."""
    @staticmethod
    def add(validated_data : dict) -> Auth:
        """Creates a regular user."""
        return Auth.objects.create_user(**validated_data)

    @staticmethod
    def add_admin(validated_data : dict) -> Auth:
        """Creates an admin user."""
        return Auth.objects.create_superuser(**validated_data)

    @staticmethod
    def add_employee(validated_data : dict) -> Auth:
        """Creates an employee user."""
        return Auth.objects.create_employee(**validated_data)

    @staticmethod
    def me(uuid : UUID) -> Auth:
        """Retrieves the authenticated user's details."""
        user = Auth.objects.filter(id=uuid).first()
        if not user:
            raise AuthServiceError('User not found', status.HTTP_404_NOT_FOUND)
        return user

    @staticmethod
    def update_last_login(user_id : UUID) -> None:
        """Updates the last login for an authenticated user."""
        user = Auth.objects.filter(id=user_id).first()
        if not user:
            raise AuthServiceError('User not found', status.HTTP_404_NOT_FOUND)
        user.last_login = now()
        user.save(update_fields=["last_login"])

    @staticmethod
    def blacklist_refresh_token(refresh_token: str) -> None:
        """Blacklists a refresh token."""
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception:
            raise AuthServiceError("The refresh token is invalid or already blacklisted.", status.HTTP_400_BAD_REQUEST)