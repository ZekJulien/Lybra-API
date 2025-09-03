from django.core.validators import RegexValidator, EmailValidator
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from auths.models import Auth

class AuthSerializer(serializers.ModelSerializer):
    """Handles user registration with email uniqueness, password strength, and confirmation validation."""
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=Auth.objects.all(),
                message="This address is already registered"
            ),
            EmailValidator()
        ]
    )
    password = serializers.CharField(
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
    password_verification = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Auth
        fields = ['email', 'password', 'password_verification', 'last_login', 'date_joined']


    def validate(self, attrs):
        if attrs['password'] != attrs['password_verification']:
            raise serializers.ValidationError("Passwords do not match.")
        attrs.pop('confirmed_password', None)
        return attrs

