from django.urls import path, include
from rest_framework import routers
from apps.books.views import AuthorViewSet

author_router = routers.DefaultRouter()
author_router.register(r'author', AuthorViewSet, basename='author')

urlpatterns = [
    path('', include(author_router.urls)),
]
