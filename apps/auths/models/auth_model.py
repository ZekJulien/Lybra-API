import uuid
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models import Q
from django.utils.timezone import now
from auths.managers import AuthManager

class Auth(AbstractBaseUser, PermissionsMixin):
    """Custom user model with email as username and role-based constraints."""
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=20, choices=[('user', 'User'), ('admin', 'Admin'), ('employee', 'Employee')], default='user')
    last_password_change = models.DateTimeField(default=now)

    objects = AuthManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    class Meta:
        app_label = 'auths'
        constraints = [
            models.UniqueConstraint(
                fields=['role'],
                condition=Q(role='admin'),
                name='unique_admin'
            )
        ]