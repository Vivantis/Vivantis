from rest_framework.routers import DefaultRouter
from .views_documentos import DocumentoViewSet

# ─────────────────────────────────────────────────────────────
# Roteador para o módulo de Documentos
# ─────────────────────────────────────────────────────────────
router = DefaultRouter()
router.register(r'documentos', DocumentoViewSet)

# Exporta as URLs para inclusão no roteador principal
urlpatterns = router.urls
