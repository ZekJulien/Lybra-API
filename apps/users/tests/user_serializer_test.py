import pytest
from apps.users.serializers import UserSerializer

@pytest.mark.django_db
def test_user_serializer_valid():
    data = {
        "username": "jdupont",
        "first_name": "Jean",
        "last_name": "Dupont",
        "street": "10 rue de la Paix",
        "postal_code": "75001",
        "city": "Paris"
    }
    serializer = UserSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    assert serializer.validated_data['username'] == "jdupont"
    assert serializer.validated_data['first_name'] == "Jean"
    assert serializer.get_level(serializer.validated_data) == 1  # xp_total par défaut 0

@pytest.mark.django_db
def test_user_serializer_missing_username():
    data = {
        "first_name": "Jean",
        "last_name": "Dupont"
    }
    serializer = UserSerializer(data=data)
    assert not serializer.is_valid()
    assert "username" in serializer.errors

@pytest.mark.django_db
def test_user_serializer_read_only_fields():
    data = {
        "username": "jdupont",
        "xp_total": 1000,
        "level": 10,  # Read-only, should be ignored on input
    }
    serializer = UserSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    # xp_total et level en read_only, ne doivent pas être dans validated_data
    assert "xp_total" not in serializer.validated_data
    assert "level" not in serializer.validated_data
