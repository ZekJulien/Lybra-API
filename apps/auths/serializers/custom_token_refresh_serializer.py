from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.tokens import AccessToken

from apps.auths.services import AuthService

class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    """Custom serializer to include user role and last password change in the refreshed token."""
    def validate(self, attrs):
        data = super().validate(attrs)
        access = AccessToken(data['access'])
        user = self.context.get('request').user if self.context.get('request') else None
        if not user or isinstance(user, AnonymousUser):
            token_backend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
            payload = token_backend.decode(attrs['refresh'], verify=False)
            user_id = payload.get('user_id')
            user = AuthService.get_user(user_id)
        access['last_password_change'] = str(user.last_password_change.timestamp())
        access['role'] = user.role
        data['access'] = str(access)
        data['role'] = str(user.role)
        return data
