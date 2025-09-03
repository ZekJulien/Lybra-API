from datetime import datetime
from uuid import UUID
from auths.models import Auth
from django.utils.timezone import now


class AuthService:
    """Service layer for user creation and management."""
    @staticmethod
    def add(validated_data : dict) -> Auth:
        """Creates a regular user."""
        return Auth.objects.create_user(**validated_data)

    @staticmethod
    def add_admin(validated_data):
        """Creates an admin user."""
        return Auth.objects.create_superuser(**validated_data)

    @staticmethod
    def add_employee(validated_data):
        """Creates an employee user."""
        return Auth.objects.create_employee(**validated_data)

    @staticmethod
    def me(uuid : UUID):
        """Retrieves the authenticated user's details."""
        return Auth.objects.filter(id=uuid).first()

    @staticmethod
    def update_last_login(user_id : UUID):
        """Updates the last login for an authenticated user."""
        user = Auth.objects.filter(id=user_id).first()
        user.last_login = now()
        user.save(update_fields=["last_login"])