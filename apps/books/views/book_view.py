from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ViewSet

from apps.auths.permissions import IsAuthenticatedWithChecks, IsEmployeeOrAdmin
from apps.books import BookPagination
from apps.books.serializers import BookSerializer, BookDetailSerializer, IsbnSerializer
from apps.books.services import BookService
from apps.books.schemas import book_viewset_schema

@book_viewset_schema
class BookViewSet(ViewSet):
    """ViewSet for managing Book entities."""
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'authors__name', 'publication_date', 'collection']

    @action(detail=False, methods=['post'], url_path='add' ,permission_classes=[IsAuthenticatedWithChecks, IsEmployeeOrAdmin])
    def add(self, request):
        """Add a new book to the database."""
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        book = BookService.add(serializer.validated_data)
        book_detail_serializer = BookDetailSerializer(book)
        return Response(book_detail_serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'], url_path=r'get_by_id/(?P<isbn>.+)')
    def get(self, request, isbn=None):
        """Retrieve a book by its ISBN."""
        serializer = IsbnSerializer(data={'isbn': isbn})
        serializer.is_valid(raise_exception=True)
        book = BookService.get_by_isbn(serializer.validated_data['isbn'])
        book_serializer = BookDetailSerializer(book)
        return Response(book_serializer.data)

    @action(detail=False, methods=['get'], url_path='get_all')
    def get_all(self, request):
        """Retrieve all books with optional filtering and pagination."""
        queryset = BookService.get_all()
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        paginator = BookPagination()
        page = paginator.paginate_queryset(queryset, request, view=self)
        if page is not None:
            serializer = BookDetailSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = BookDetailSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['put'], url_path='update_book', permission_classes=[IsAuthenticatedWithChecks, IsEmployeeOrAdmin])
    def update_book(self, request):
        """ Update an existing book's details."""
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        book = BookService.update(serializer.validated_data)
        response_serializer = BookDetailSerializer(book)
        return Response(response_serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['delete'], url_path=r'delete/(?P<isbn>.+)',
            permission_classes=[IsAuthenticatedWithChecks, IsEmployeeOrAdmin])
    def delete_book(self, request, isbn=None):
        serializer = IsbnSerializer(data={'isbn': isbn})
        serializer.is_valid(raise_exception=True)
        BookService.delete(serializer.validated_data['isbn'])
        return Response(status=status.HTTP_204_NO_CONTENT)