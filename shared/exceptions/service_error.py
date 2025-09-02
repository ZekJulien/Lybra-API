from rest_framework import status

class ServiceError(Exception):
    def __init__(self, message="A service error occurred", status_code = status.HTTP_400_BAD_REQUEST, code=None):
        self.message = message
        self.status_code = status_code
        self.code = code
        super().__init__(message)
