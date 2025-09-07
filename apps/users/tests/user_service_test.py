import pytest
from uuid import uuid4
from apps.users.services.user_service import UserService, UserServiceError
from apps.auths.models import Auth
from apps.users.models import User
from apps.users.enums import UserMessage

@pytest.mark.django_db
def test_add_user_success():
    auth = Auth.objects.create_user(email="auth@example.com", password="Test12345")
    data = {
        "username": "uniqueuser",
        "first_name": "Jean",
        "last_name": "Dupont",
        "street": "Some street",
        "postal_code": "75001",
        "city": "Paris",
    }
    user = UserService.add(auth, data)
    assert user.id == auth
    assert user.username == "uniqueuser"

@pytest.mark.django_db
def test_add_user_existing_user_raises():
    auth = Auth.objects.create_user(email="auth2@example.com", password="Test12345")
    User.objects.create(id=auth, username="alreadyexists")
    data = {
        "username": "newuser",
    }
    with pytest.raises(UserServiceError) as excinfo:
        UserService.add(auth, data)
    assert excinfo.value.args[0] == UserMessage.USER_EXISTS.value

@pytest.mark.django_db
def test_add_user_existing_username_raises():
    auth1 = Auth.objects.create_user(email="auth3@example.com", password="Test12345")
    auth2 = Auth.objects.create_user(email="auth4@example.com", password="Test12345")
    User.objects.create(id=auth1, username="takenusername")
    data = {
        "username": "takenusername",
    }
    with pytest.raises(UserServiceError) as excinfo:
        UserService.add(auth2, data)
    assert excinfo.value.args[0] == UserMessage.USERNAME_TAKEN.value
