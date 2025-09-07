from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status

from apps.auths.permissions import IsAuthenticatedWithChecks
from apps.users.enums import UserMessage
from apps.users.schemas import user_schema
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