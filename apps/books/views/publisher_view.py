from rest_framework import viewsets
from apps.auths.permissions import IsAuthenticatedWithChecks
from apps.books.models import Publisher
from apps.books.serializers import PublisherSerializer
from apps.auths.permissions import IsEmployeeOrAdmin
from apps.books.schemas import publisher_viewset_schema

@publisher_viewset_schema
class PublisherViewSet(viewsets.ModelViewSet):
    """ViewSet for managing publishers."""
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [IsAuthenticatedWithChecks, IsEmployeeOrAdmin]
