from rest_framework.routers import DefaultRouter
from .views import ReservaEspacoViewSet  # importa do views.py, não views_reservas.py

# ─────────────────────────────────────────────────────────────
# Roteador para o módulo de Reservas de Espaço
# ─────────────────────────────────────────────────────────────
router = DefaultRouter()
router.register(r'reservas', ReservaEspacoViewSet, basename='reservas')

# Exporta as URLs para inclusão no roteador principal
urlpatterns = router.urls
