from rest_framework.routers import DefaultRouter
from .views import AvisoViewSet


# ─────────────────────────────────────────────────────────────
# Roteador para o módulo de Avisos e Comunicados
# ─────────────────────────────────────────────────────────────
router = DefaultRouter()
router.register(r'avisos', AvisoViewSet)

# Exporta as URLs para o roteador principal
urlpatterns = router.urls
