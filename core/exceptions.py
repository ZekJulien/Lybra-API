from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

from shared.exceptions.service_error import ServiceError


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        return response

    if isinstance(exc, ServiceError):
        error_type = exc.__class__.__name__
        return Response(
            {
                "detail": exc.message,
                "code": exc.code,
                "type": error_type
            },
            status=exc.status_code
        )

    return Response(
        {"detail": "An unexpected error occurred. Please try again later."},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )
