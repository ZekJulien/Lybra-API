import pytest
from rest_framework.test import APIClient
from auths.services import AuthService
from auths.models import Auth

@pytest.mark.django_db
def test_create_admin_success():
    data = {
        "email": "admin@example.com",
        "password": "Secure123A",
        "password_verification": "Secure123A"
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
        "password_verification": "Secure123A"
    }
    data2 = {
        "email": "admin2@example.com",
        "password": "Secure123A",
        "password_verification": "Secure123A"
    }

    AuthService.add_admin(data1)

    with pytest.raises(ValueError):
        AuthService.add_admin(data2)

@pytest.mark.django_db
def test_create_employee():
    admin = AuthService.add_admin({
        "email": "admin@example.com",
        "password": "Secure123A",
        "password_verification": "Secure123A"
    })

    data = {
        "email": "employee@example.com",
        "password": "Secure123A",
        "password_verification": "Secure123A"
    }

    employee = AuthService.add_employee(data)

    assert employee.email == data["email"]
    assert employee.role == "employee"

@pytest.mark.django_db
def test_create_user():
    data = {
        "email": "user@example.com",
        "password": "Secure123A",
        "password_verification": "Secure123A"
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
