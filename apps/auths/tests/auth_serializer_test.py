import pytest
from apps.auths.serializers import AuthSerializer
from apps.auths.models import Auth

@pytest.mark.django_db
def test_valid_password():
    data = {
        "email": "valid@example.com",
        "password": "Secure123",
        "password_verification": "Secure123"
    }
    serializer = AuthSerializer(data=data)
    assert serializer.is_valid()

@pytest.mark.django_db
@pytest.mark.parametrize("password", [
    "short1A",            # trop court
    "alllowercase1",      # pas de majuscule
    "NoDigitsHere",       # pas de chiffre
])
def test_invalid_password_regex(password):
    data = {
        "email": "fail@example.com",
        "password": password,
        "password_verification": password
    }
    serializer = AuthSerializer(data=data)
    assert not serializer.is_valid()
    assert "password" in serializer.errors

@pytest.mark.django_db
def test_password_mismatch():
    data = {
        "email": "mismatch@example.com",
        "password": "Secure123",
        "password_verification": "Secure321"
    }
    serializer = AuthSerializer(data=data)
    assert not serializer.is_valid()
    assert "non_field_errors" in serializer.errors

@pytest.mark.django_db
def test_email_already_exists():
    Auth.objects.create_user(email="duplicate@example.com", password="Secure123")
    data = {
        "email": "duplicate@example.com",
        "password": "Secure123",
        "password_verification": "Secure123"
    }
    serializer = AuthSerializer(data=data)
    assert not serializer.is_valid()
    assert "email" in serializer.errors

