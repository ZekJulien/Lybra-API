from rest_framework import viewsets
from apps.auths.permissions import IsAuthenticatedWithChecks, IsEmployeeOrAdmin
from apps.books.models import BookCopy
from apps.books.serializers import BookCopySerializer
from apps.books.schemas import bookcopy_viewset_schema

@bookcopy_viewset_schema
class BookCopyViewSet(viewsets.ModelViewSet):
    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer
    permission_classes = [IsAuthenticatedWithChecks, IsEmployeeOrAdmin]
