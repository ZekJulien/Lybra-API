from rest_framework import viewsets

from apps.auths.permissions import IsAuthenticatedWithChecks, IsEmployeeOrAdmin
from apps.books.models import Collection
from apps.books.serializers import CollectionSerializer
from apps.books.schemas import collection_viewset_schema


@collection_viewset_schema
class CollectionViewSet(viewsets.ModelViewSet):
    """ViewSet for managing collections."""
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [IsAuthenticatedWithChecks, IsEmployeeOrAdmin]
