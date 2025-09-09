from rest_framework import viewsets
from apps.books.models import Genre
from apps.books.serializers import GenreSerializer
from apps.auths.permissions import IsAuthenticatedWithChecks, IsEmployeeOrAdmin
from apps.books.schemas import genre_viewset_schema


@genre_viewset_schema
class GenreViewSet(viewsets.ModelViewSet):
    """ViewSet for managing genres."""
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticatedWithChecks, IsEmployeeOrAdmin]