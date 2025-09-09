from rest_framework import viewsets

from apps.auths.permissions import IsAuthenticatedWithChecks, IsEmployeeOrAdmin
from apps.books.models import Theme
from apps.books.serializers import ThemeSerializer
from apps.books.schemas import theme_viewset_schema


@theme_viewset_schema
class ThemeViewSet(viewsets.ModelViewSet):
    """ViewSet for managing themes."""
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    permission_classes = [IsAuthenticatedWithChecks, IsEmployeeOrAdmin]
