from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PrestadorViewSet

router = DefaultRouter()
router.register(r'', PrestadorViewSet, basename='prestador')

urlpatterns = [
    path('', include(router.urls)),
]
