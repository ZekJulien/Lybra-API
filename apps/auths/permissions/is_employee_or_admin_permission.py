from rest_framework.permissions import BasePermission

class IsEmployeeOrAdmin(BasePermission):
    """Allows access only to admin users."""
    def has_permission(self, request, view):
        user = request.user
        return user and user.is_authenticated and user.role == 'admin' or user.role == 'employee'
