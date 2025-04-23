from rest_framework.routers import DefaultRouter
from .views import ControleAcessoViewSet  # Ajuste: importa de views.py

# ─────────────────────────────────────────────────────────────
# Roteador para o módulo de Controle de Acesso
# ─────────────────────────────────────────────────────────────
router = DefaultRouter()
router.register(r'controle-acesso', ControleAcessoViewSet, basename='controle-acesso')

# Exporta as URLs para inclusão no roteador principal
urlpatterns = router.urls
