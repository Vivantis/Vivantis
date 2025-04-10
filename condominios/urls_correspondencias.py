from rest_framework.routers import DefaultRouter
from .views_correspondencias import CorrespondenciaViewSet  # Importa o ViewSet de Correspondência

# ─────────────────────────────────────────────────────────────
# Roteador padrão do DRF
# ─────────────────────────────────────────────────────────────
router = DefaultRouter()

# Registra o endpoint 'correspondencias' (prefixo da rota)
# Gera: /api/correspondencias/, /api/correspondencias/{id}/, etc.
router.register(r'correspondencias', CorrespondenciaViewSet)

# ─────────────────────────────────────────────────────────────
# Expõe as rotas para inclusão no roteador principal
# ─────────────────────────────────────────────────────────────
urlpatterns = router.urls
