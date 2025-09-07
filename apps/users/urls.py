from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.users.views import UserView

router = DefaultRouter()
router.register(r'', UserView, basename='user')

urlpatterns = [
    path('', include(router.urls))
]