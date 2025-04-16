from rest_framework.routers import DefaultRouter
from .views_acesso import ControleAcessoViewSet  # ViewSet do módulo de Acesso

# 🔧 Roteador padrão do DRF
router = DefaultRouter()

# 🚪 Endpoint: /api/acessos/
router.register(r'acessos', ControleAcessoViewSet, basename='acesso')

# 🌐 URLs geradas automaticamente
urlpatterns = router.urls
from rest_framework.routers import DefaultRouter
from .views_acesso import ControleAcessoViewSet  # ViewSet do módulo de Acesso

# 🔧 Roteador padrão do DRF
router = DefaultRouter()

# 🚪 Endpoint: /api/acessos/
router.register(r'acessos', ControleAcessoViewSet, basename='acesso')

# 🌐 URLs geradas automaticamente
urlpatterns = router.urls
