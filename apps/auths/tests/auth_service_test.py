import pytest
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
