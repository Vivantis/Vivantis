from rest_framework.routers import DefaultRouter
from .views import CobrancaViewSet  # Ajuste: importa de views.py

# ─────────────────────────────────────────────────────────────
# Roteador para o módulo de Cobranças
# ─────────────────────────────────────────────────────────────
router = DefaultRouter()
router.register(r'cobrancas', CobrancaViewSet, basename='cobrancas')

# Exporta as URLs para inclusão no roteador principal
urlpatterns = router.urls
