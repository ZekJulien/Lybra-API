from rest_framework.permissions import BasePermission
from auths.models import Auth

class IsFirstUser(BasePermission):
    def has_permission(self, request, view):
        return Auth.objects.count() == 0

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user and user.is_authenticated and user.role == 'admin'
