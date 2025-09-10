from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.auths.permissions import IsAuthenticatedWithChecks, IsEmployeeOrAdmin
from apps.books.serializers import BookSerializer
from apps.books.services import BookService
from apps.books.schemas import book_viewset_schema
from books.serializers.book_detail_serializer import BookDetailSerializer


@book_viewset_schema
class BookViewSet(viewsets.ViewSet):
    """ViewSet for managing Book entities."""
    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticatedWithChecks, IsEmployeeOrAdmin])
    def add(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        book = BookService.add(serializer.validated_data)
        book_detail_serializer = BookDetailSerializer(book)
        return Response(book_detail_serializer.data, status=status.HTTP_201_CREATED)