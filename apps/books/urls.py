from django.urls import path, include
from rest_framework import routers
from apps.books.views import AuthorViewSet, PublisherViewSet, GenreViewSet, ThemeViewSet

author_router = routers.DefaultRouter()
author_router.register(r'author', AuthorViewSet, basename='author')

publisher_router = routers.DefaultRouter()
publisher_router.register(r'publisher', PublisherViewSet, basename='publisher')

genre_router = routers.DefaultRouter()
genre_router.register(r'genre', GenreViewSet, basename='genre')

theme_router = routers.DefaultRouter()
theme_router.register(r'theme', ThemeViewSet, basename='theme')

urlpatterns = [
    path('', include(author_router.urls)),
    path('', include(publisher_router.urls)),
    path('', include(genre_router.urls)),
    path('', include(theme_router.urls)),
]
