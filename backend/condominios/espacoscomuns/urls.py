from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_reservas import EspacoComumViewSet  # Views ainda ficam em views_reservas.py

# 🔧 Roteador DRF
router = DefaultRouter()
router.register(r'espacos-comuns', EspacoComumViewSet)

# 🌐 URLs expostas para inclusão no core
urlpatterns = [
    path('', include(router.urls)),
]
