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

    error_type = exc.__class__.__name__
    error_message = str(exc)

    fallback_status = status.HTTP_400_BAD_REQUEST if error_type.endswith(
        "Error") else status.HTTP_500_INTERNAL_SERVER_ERROR

    return Response(
        {
            "detail": error_message,
            "type": error_type
        },
        status=fallback_status
    )
