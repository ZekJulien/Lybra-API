from django.urls import path, include
from rest_framework.routers import DefaultRouter
from auths.views import AuthView

router = DefaultRouter()
router.register(r'', AuthView, basename='auths')

urlpatterns = [
    path('', include(router.urls))
]