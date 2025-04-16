from rest_framework.routers import DefaultRouter
from .views_administradores import AdministradorGeralViewSet

# ─────────────────────────────────────────────────────────────
# Roteador para o módulo de Administradores Gerais
# ─────────────────────────────────────────────────────────────
router = DefaultRouter()
router.register(r'administradores', AdministradorGeralViewSet)

# Exporta as URLs para o roteador principal
urlpatterns = router.urls

