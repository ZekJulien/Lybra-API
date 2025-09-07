from enum import Enum

class UserMessage(Enum):
    """Enum for user-related messages."""
    USER_NOT_FOUND = 'Utilisateur non existant.'
    USERNAME_TAKEN = 'Le nom d’utilisateur est déjà pris.'
    INVALID_DATA = 'Données invalides.'
    USER_CREATED = 'Utilisateur créé avec succès.'
    USER_UPDATED = 'Utilisateur mis à jour.'
    USER_EXISTS = 'Utilisateur existant.'
