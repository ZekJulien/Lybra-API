from rest_framework.pagination import PageNumberPagination

class BookPagination(PageNumberPagination):
    """Custom pagination class for books."""
    page_size = 10
