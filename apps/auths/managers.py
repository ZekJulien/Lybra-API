from django.contrib.auth.base_user import BaseUserManager

class AuthManager(BaseUserManager):
    """Custom manager for Auth model with role-based user creation methods."""
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a regular user with the given email and password."""
        if not email:
            raise ValueError('Email must be set')
        email = self.normalize_email(email)
        auth = self.model(email=email, **extra_fields)
        auth.set_password(password)
        auth.save(using=self._db)
        return auth

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        Ensures only one admin user exists.
        The first user created can be an admin, else raises an error.
        """
        if self.model.objects.filter(role='admin').exists():
            raise ValueError('Only one admin allowed')
        extra_fields.setdefault('role', 'admin')
        return self.create_user(email, password, **extra_fields)

    def create_employee(self, email, password=None, **extra_fields):
        """
        Creates and saves an employee user with the given email and password.
        Ensures the role is set to 'employee'.
        """
        extra_fields.setdefault('role', 'employee')
        return self.create_user(email, password, **extra_fields)
