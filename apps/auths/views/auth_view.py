from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiResponse

from auths.serializers import AuthSerializer
from auths.services import AuthService
from auths.permissions import IsFirstUser, IsAdminUser

class AuthView(ViewSet):

    @extend_schema(
        request=AuthSerializer,
        responses={
            200: OpenApiResponse(
              description="Account created successfully"
            )
          },
        summary="Initialize the first administrator"
    )
    @action(detail=False, methods=['post'], url_path='init', permission_classes=[IsFirstUser])
    def init_admin(self, request):
        serializer = AuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        AuthService.add_admin(serializer.validated_data)
        return Response({ "message": "Account created successfully" }, status=status.HTTP_200_OK)

    @extend_schema(
        request=AuthSerializer,
        responses={
            200: OpenApiResponse(
                description="Account created successfully"
            )
        },
        summary="Create a new user"
    )
    @action(detail=False, methods=['post'], url_path='register')
    def create_user(self, request):
        serializer = AuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        AuthService.add(serializer.validated_data)
        return Response({ "message": "Account created successfully" }, status=status.HTTP_200_OK)

    @extend_schema(
        request=AuthSerializer,
        responses={
            200: OpenApiResponse(
                description="Account created successfully"
            )
        },
        summary="Create a new employee"
    )
    @action(detail=False, methods=['post'], url_path='employee', permission_classes=[IsAdminUser])
    def create_employee(self, request):
        serializer = AuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        AuthService.add_employee(serializer.validated_data)
        return Response({ "message": "Account created successfully" }, status=status.HTTP_200_OK)
