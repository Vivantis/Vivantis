# condominios/urls_reservas.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_reservas import ReservaEspacoViewSet  # Certifique-se de ter esse arquivo com a view

# 🔧 Roteador padrão do DRF
router = DefaultRouter()

# Registra o endpoint de reservas
router.register(r'reservas', ReservaEspacoViewSet)

# 🌐 URLs expostas para inclusão no roteador principal
urlpatterns = [
    path('', include(router.urls)),
]
