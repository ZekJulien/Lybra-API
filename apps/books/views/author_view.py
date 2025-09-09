from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from apps.auths.permissions import IsAuthenticatedWithChecks, IsEmployeeOrAdmin
from apps.books.models import Author
from apps.books.serializers import AuthorSerializer

@extend_schema_view(
    list=extend_schema(summary="List all authors", description="Retrieve a list of all authors."),
    retrieve=extend_schema(summary="Get a specific author", description="Retrieve details of an author by their ID."),
    create=extend_schema(summary="Create a new author", description="Add a new author with the provided information."),
    update=extend_schema(summary="Update an author", description="Update the details of an existing author."),
    partial_update=extend_schema(summary="Partially update an author", description="Update some fields of an existing author."),
    destroy=extend_schema(summary="Delete an author", description="Delete an author by their ID."),
)
class AuthorViewSet(viewsets.ModelViewSet):
    '''ViewSet for managing authors.'''
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedWithChecks ,IsEmployeeOrAdmin]
