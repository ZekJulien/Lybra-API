from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User model, including a computed level field."""
    level = serializers.SerializerMethodField()
    username = serializers.CharField(
        validators=[]
    )

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'street',
            'postal_code',
            'city',
            'xp_total',
            'level'
        ]
        read_only_fields = ['id', 'level', 'xp_total']

    @extend_schema_field(int)
    def get_level(self, obj):
        """Compute the level of the user."""
        xp = obj.get('xp_total') if isinstance(obj, dict) else getattr(obj, 'xp_total', 0)
        if xp is None:
            xp = 0
        return (xp // 1000) + 1