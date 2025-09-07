from uuid import UUID

from apps.auths.models import Auth
from apps.users.enums import UserMessage
from apps.users.models import User
from apps.users.types import UserPayload
from shared.exceptions.user_service_error import UserServiceError
from rest_framework import status


class UserService:
    """Service class for managing user-related operations."""
    @staticmethod
    def is_unique_username(username) -> bool:
        """Check if a username is already taken."""
        return User.objects.filter(username=username).exists()

    @staticmethod
    def is_unique_user(user_id: UUID) -> bool:
        """Check if a user exists."""
        return User.objects.filter(id=user_id).exists()

    @staticmethod
    def add(auth: Auth, validated_data : UserPayload) -> User:
        """Add a new user to the database."""
        print(auth.id)
        if UserService.is_unique_user(auth.id):
            raise UserServiceError(UserMessage.USER_EXISTS.value, code=status.HTTP_409_CONFLICT)
        if UserService.is_unique_username(validated_data['username']):
            raise UserServiceError(UserMessage.USERNAME_TAKEN.value, code=status.HTTP_409_CONFLICT)
        return User.objects.create(id=auth, **validated_data)
