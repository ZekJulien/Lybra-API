from auths.models import Auth

class AuthService:
    @staticmethod
    def add(validated_data):
        validated_data.pop('password_verification')
        return Auth.objects.create_user(**validated_data)

    @staticmethod
    def add_admin(validated_data):
        validated_data.pop('password_verification')
        return Auth.objects.create_superuser(**validated_data)

    @staticmethod
    def add_employee(validated_data):
        validated_data.pop('password_verification')
        return Auth.objects.create_employee(**validated_data)
