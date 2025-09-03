from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer

from auths.schemas import auth_schema
from auths.serializers import AuthSerializer
from auths.services import AuthService
from auths.permissions import IsFirstUser, IsAdminUser

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
        serializer = TokenObtainPairSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], url_path='token/refresh')
    def token_refresh(self, request):
        serializer = TokenRefreshSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)