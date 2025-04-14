# condominios/urls_reservas.py

from rest_framework.routers import DefaultRouter
from .views_reservas import EspacoComumViewSet, ReservaEspacoViewSet

# ─────────────────────────────────────────────────────────────
# 🔁 Roteador exclusivo para espaços comuns e reservas
# ─────────────────────────────────────────────────────────────
router = DefaultRouter()

# Endpoint para gerenciar os espaços disponíveis no condomínio
# Ex: /api/espacos/
router.register(r'espacos', EspacoComumViewSet)

# Endpoint para criar, listar e acompanhar reservas
# Ex: /api/reservas/
router.register(r'reservas', ReservaEspacoViewSet)

# ─────────────────────────────────────────────────────────────
# 🌐 Exporta as rotas para serem incluídas no urls.py principal
# ─────────────────────────────────────────────────────────────
urlpatterns = router.urls
