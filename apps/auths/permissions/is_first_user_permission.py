from rest_framework.permissions import BasePermission
from apps.auths.models import Auth

class IsFirstUser(BasePermission):
    """Allows access only if no users exist in the system."""
    def has_permission(self, request, view):
        return Auth.objects.count() == 0