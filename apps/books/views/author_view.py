from rest_framework import viewsets

from apps.auths.permissions import IsAuthenticatedWithChecks, IsEmployeeOrAdmin
from apps.books.models import Author
from apps.books.serializers import AuthorSerializer
from apps.books.schemas import author_viewset_schema

@author_viewset_schema
class AuthorViewSet(viewsets.ModelViewSet):
    """ViewSet for managing authors."""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedWithChecks ,IsEmployeeOrAdmin]
