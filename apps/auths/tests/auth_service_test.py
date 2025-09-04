from uuid import uuid4

import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken

from auths.services import AuthService
from auths.models import Auth
from shared.exceptions import AuthServiceError
from rest_framework import status

@pytest.mark.django_db
def test_create_admin_success():
    data = {
        "email": "admin@example.com",
        "password": "Secure123A",
    }

    admin = AuthService.add_admin(data)

    assert admin.email == data["email"]
    assert admin.role == "admin"
    assert Auth.objects.filter(role="admin").count() == 1

@pytest.mark.django_db
def test_create_second_admin_should_fail():
    data1 = {
        "email": "admin1@example.com",
        "password": "Secure123A",
    }
    data2 = {
        "email": "admin2@example.com",
        "password": "Secure123A",
    }

    AuthService.add_admin(data1)

    with pytest.raises(ValueError):
        AuthService.add_admin(data2)

@pytest.mark.django_db
def test_create_employee():
    admin = AuthService.add_admin({
        "email": "admin@example.com",
        "password": "Secure123A",
    })

    data = {
        "email": "employee@example.com",
        "password": "Secure123A",
    }

    employee = AuthService.add_employee(data)

    assert employee.email == data["email"]
    assert employee.role == "employee"

@pytest.mark.django_db
def test_create_user():
    data = {
        "email": "user@example.com",
        "password": "Secure123A",
    }

    employee = AuthService.add(data)

    assert employee.email == data["email"]
    assert employee.role == "user"

@pytest.mark.django_db
def test_token_obtain_success():
    client = APIClient()

    Auth.objects.create_user(
        email="user@example.com",
        password="Secure123A"
    )

    response = client.post("/auth/token/", {
        "email": "user@example.com",
        "password": "Secure123A"
    })

    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data

@pytest.mark.django_db
def test_token_refresh_success():
    client = APIClient()

    user = Auth.objects.create_user(
        email="user@example.com",
        password="Secure123A"
    )

    token_response = client.post("/auth/token/", {
        "email": "user@example.com",
        "password": "Secure123A"
    })

    refresh_token = token_response.data["refresh"]

    response = client.post("/auth/token/refresh/", {
        "refresh": refresh_token
    })

    assert response.status_code == 200
    assert "access" in response.data

@pytest.mark.django_db
def test_auth_service_me_returns_user():
    user = Auth.objects.create_user(
        email="test@example.com",
        password="securepassword123"
    )

    result = AuthService.me(user.id)

    assert result is not None
    assert result.id == user.id
    assert result.email == "test@example.com"

@pytest.mark.django_db
def test_auth_service_me_raises_for_unknown_uuid():
    unknown_uuid = uuid4()

    with pytest.raises(AuthServiceError) as exc_info:
        AuthService.me(unknown_uuid)

    exc = exc_info.value
    assert exc.status_code == status.HTTP_404_NOT_FOUND
    assert "User not found" in str(exc)

@pytest.mark.django_db
def test_me_user_not_found():
    with pytest.raises(AuthServiceError) as exc_info:
        AuthService.me(uuid=uuid4())
    assert exc_info.value.status_code == 404
    assert "User not found" in str(exc_info.value)

@pytest.mark.django_db
def test_blacklist_refresh_token_valid():
    user = Auth.objects.create_user(email="test@example.com", password="secure123")
    refresh = RefreshToken.for_user(user)
    token_str = str(refresh)

    AuthService.blacklist_refresh_token(token_str)

    jti = refresh["jti"]
    assert BlacklistedToken.objects.filter(token__jti=jti).exists()

@pytest.mark.django_db
def test_blacklist_refresh_token_invalid():
    invalid_token = "this.is.not.a.valid.token"

    with pytest.raises(AuthServiceError) as exc_info:
        AuthService.blacklist_refresh_token(invalid_token)

    exc = exc_info.value
    assert exc.status_code == status.HTTP_400_BAD_REQUEST
    assert "invalid or already blacklisted" in str(exc)

@pytest.mark.django_db
def test_password_change_updates_timestamp():
    user = Auth.objects.create_user(email="test@example.com", password="secure123")
    old_timestamp = user.last_password_change

    AuthService.update_password(user.id, "secure123", "newSecure123")

    user.refresh_from_db()
    assert user.last_password_change > old_timestamp
