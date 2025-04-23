from rest_framework.routers import DefaultRouter
from .views import CorrespondenciaViewSet  # IMPORT CORRETO

# ─────────────────────────────────────────────────────────────
# Roteador para o módulo de Correspondências
# ─────────────────────────────────────────────────────────────
router = DefaultRouter()
router.register(r'correspondencias', CorrespondenciaViewSet, basename='correspondencias')

# Exporta as URLs para inclusão no roteador principal
urlpatterns = router.urls
