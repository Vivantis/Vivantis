from rest_framework.routers import DefaultRouter
from .views_manutencao import ManutencaoViewSet

# ─────────────────────────────────────────────────────────────
# Roteador para o módulo de Agenda de Manutenções
# ─────────────────────────────────────────────────────────────
router = DefaultRouter()
router.register(r'manutencao', ManutencaoViewSet)

# Exporta as URLs para o roteador principal
urlpatterns = router.urls
