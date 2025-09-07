from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from apps.auths.models import Auth

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Custom serializer to include user role in the token and response."""
    def validate(self, attrs):
        data = super().validate(attrs)
        data["role"] = str(self.user.role)
        return data

    @classmethod
    def get_token(cls, user : Auth):
        token = super().get_token(user)
        token["last_password_change"] = str(user.last_password_change.timestamp())
        token["role"] = str(user.role)
        return token
