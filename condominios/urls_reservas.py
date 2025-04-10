from rest_framework.routers import DefaultRouter
from .views_reservas import EspacoComumViewSet, ReservaEspacoViewSet

# ─────────────────────────────────────────────────────────────
# Roteador para espaços comuns e reservas
# ─────────────────────────────────────────────────────────────
router = DefaultRouter()

# Endpoint para gerenciar os espaços disponíveis no condomínio
router.register(r'espacos', EspacoComumViewSet)

# Endpoint para criar e acompanhar reservas de moradores
router.register(r'reservas', ReservaEspacoViewSet)

# ─────────────────────────────────────────────────────────────
# Exporta as rotas para o roteador principal
# ─────────────────────────────────────────────────────────────
urlpatterns = router.urls
