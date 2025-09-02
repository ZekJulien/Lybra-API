from auths.models import Auth

class AuthService:
    """Service layer for user creation and management."""
    @staticmethod
    def add(validated_data):
        """Creates a regular user."""
        validated_data.pop('password_verification')
        return Auth.objects.create_user(**validated_data)

    @staticmethod
    def add_admin(validated_data):
        """Creates an admin user."""
        validated_data.pop('password_verification')
        return Auth.objects.create_superuser(**validated_data)

    @staticmethod
    def add_employee(validated_data):
        """Creates an employee user."""
        validated_data.pop('password_verification')
        return Auth.objects.create_employee(**validated_data)
