# condominios/urls_auditoria.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_auditoria import AuditoriaViewSet

router = DefaultRouter()
router.register(r'auditorias', AuditoriaViewSet, basename='auditoria')

urlpatterns = [
    path('', include(router.urls)),
]
