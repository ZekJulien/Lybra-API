from django.core.validators import RegexValidator
from rest_framework import serializers

class UpdatePasswordSerializers(serializers.Serializer):
    """Serializer for handling password change requests."""
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[
            RegexValidator(
                regex=r'^(?=.*[A-Z])(?=.*\d).{8,}$',
                message='Password must be at least 8 characters long, '
                        'contain one uppercase letter and one digit.'
            )
        ]
    )