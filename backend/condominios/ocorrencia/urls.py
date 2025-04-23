from rest_framework.routers import DefaultRouter
from .views import OcorrenciaViewSet  # Ajuste: importa de views.py

# ─────────────────────────────────────────────────────────────
# Roteador para o módulo de Ocorrências
# ─────────────────────────────────────────────────────────────
router = DefaultRouter()
router.register(r'ocorrencias', OcorrenciaViewSet, basename='ocorrencias')

# Exporta as URLs para inclusão no roteador principal
urlpatterns = router.urls
