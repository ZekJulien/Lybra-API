from django.urls import path, include
from rest_framework import routers
from apps.books.views import AuthorViewSet, PublisherViewSet, GenreViewSet, ThemeViewSet, CollectionViewSet, BookViewSet

router = routers.DefaultRouter()
router.register('author', AuthorViewSet)
router.register('publisher', PublisherViewSet)
router.register('genre', GenreViewSet)
router.register('theme', ThemeViewSet)
router.register('collection', CollectionViewSet)
router.register('', BookViewSet, basename='book')


urlpatterns = [
    path('', include(router.urls)),
]
