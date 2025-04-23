from rest_framework.routers import DefaultRouter
from .views import VisitanteViewSet  # Ajuste: importa de views.py

# ─────────────────────────────────────────────────────────────
# Roteador para o módulo de Visitantes
# ─────────────────────────────────────────────────────────────
router = DefaultRouter()
router.register(r'visitantes', VisitanteViewSet, basename='visitantes')

# Exporta as URLs para inclusão no roteador principal
urlpatterns = router.urls
