from rest_framework import serializers

class LogoutRequestSerializer(serializers.Serializer):
    """Serializer for logout requests."""
    refresh = serializers.CharField(help_text="Blacklist refresh token")
