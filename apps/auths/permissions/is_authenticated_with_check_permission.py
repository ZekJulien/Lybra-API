from rest_framework.permissions import IsAuthenticated

class IsAuthenticatedWithChecks(IsAuthenticated):
    """Custom permission class that checks if the user is authenticated and if the token is valid and active user."""
    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False

        token = request.auth
        user = request.user

        if not token or not user:
            return False

        if not user.is_active:
            return False

        token_last_change = token.get('last_password_change')
        if not token_last_change:
            return False

        actual_last_change = user.last_password_change.timestamp()
        return float(token_last_change) >= actual_last_change
