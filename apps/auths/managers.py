from django.contrib.auth.base_user import BaseUserManager

class AuthManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email must be set')
        email = self.normalize_email(email)
        auth = self.model(email=email, **extra_fields)
        auth.set_password(password)
        auth.save(using=self._db)
        return auth

    def create_superuser(self, email, password=None, **extra_fields):
        if self.model.objects.filter(role='admin').exists():
            raise ValueError('Only one admin allowed')
        extra_fields.setdefault('role', 'admin')
        return self.create_user(email, password, **extra_fields)

    def create_employee(self, email, password=None, **extra_fields):
        extra_fields.setdefault('role', 'employee')
        return self.create_user(email, password, **extra_fields)
