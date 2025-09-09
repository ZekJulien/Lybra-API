from django.urls import path, include
from rest_framework import routers
from apps.books.views import AuthorViewSet
from apps.books.views import PublisherViewSet

author_router = routers.DefaultRouter()
author_router.register(r'author', AuthorViewSet, basename='author')

publisher_router = routers.DefaultRouter()
publisher_router.register(r'publisher', PublisherViewSet, basename='publisher')

urlpatterns = [
    path('', include(author_router.urls)),
    path('', include(publisher_router.urls)),
]
