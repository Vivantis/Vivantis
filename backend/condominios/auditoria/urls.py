from rest_framework.routers import DefaultRouter
from .views import AuditoriaViewSet  # Ajuste: importa de views.py

# ─────────────────────────────────────────────────────────────
# Roteador para o módulo de Auditoria
# ─────────────────────────────────────────────────────────────
router = DefaultRouter()
router.register(r'auditoria', AuditoriaViewSet, basename='auditoria')

# Exporta as URLs para inclusão no roteador principal
urlpatterns = router.urls
