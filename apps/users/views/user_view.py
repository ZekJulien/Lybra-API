from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status

from apps.auths.permissions import IsAuthenticatedWithChecks, IsAdminUser
from apps.auths.permissions.is_employee_or_admin_permission import IsEmployeeOrAdmin
from apps.users.enums import UserMessage
from apps.users.schemas import user_schema, get_by_id_schema
from apps.users.serializers import UserSerializer
from apps.users.services.user_service import UserService

@user_schema
class UserView(ViewSet):
    """ViewSet for user-related operations."""
    @action(detail=False, methods=['post'], url_path='add', permission_classes=[IsAuthenticatedWithChecks])
    def add(self, request):
        """Endpoint to add a new user."""
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = UserService.add(request.user, serializer.validated_data)
        return Response(serializer.data(user), status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'], url_path='get', permission_classes=[IsAuthenticatedWithChecks])
    def get(self, request):
        """Endpoint to get a user."""
        user = UserService.get_by_id(request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @get_by_id_schema
    @action(detail=False, methods=['get'], url_path=r'get_by_id/(?P<user_id>[0-9a-f-]{36})',
            permission_classes=[IsAuthenticatedWithChecks, IsEmployeeOrAdmin])
    def get_by_id(self, request, user_id=None):
        """Endpoint to get a user by ID with pk in the route."""
        if not user_id:
            return Response(UserMessage.MISSING_PARAMS.value, status=status.HTTP_400_BAD_REQUEST)
        user = UserService.get_by_id(user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='get/all', permission_classes=[IsAuthenticatedWithChecks, IsAdminUser])
    def get_all_users(self, request):
        """Retrieve all users."""
        serializer = UserSerializer(UserService.get_all_users(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
