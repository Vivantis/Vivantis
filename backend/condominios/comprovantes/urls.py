from rest_framework.routers import DefaultRouter
from .views import ComprovantePagamentoViewSet  # Ajuste: importa de views.py

# ─────────────────────────────────────────────────────────────
# Roteador para o módulo de Comprovantes de Pagamento
# ─────────────────────────────────────────────────────────────
router = DefaultRouter()
router.register(r'comprovantes', ComprovantePagamentoViewSet, basename='comprovantes')

# Exporta as URLs para inclusão no roteador principal
urlpatterns = router.urls
