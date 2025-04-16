# condominios/urls_autorizacoes.py

from rest_framework.routers import DefaultRouter
from .views_autorizacoes import AutorizacaoEntradaViewSet

# 🔧 Roteador padrão do DRF para o módulo de Autorizações
router = DefaultRouter()
router.register(r'autorizacoes', AutorizacaoEntradaViewSet)

# 🌐 Exporta as URLs para inclusão no roteador principal
urlpatterns = router.urls
