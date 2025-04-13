from rest_framework.routers import DefaultRouter
from .views_acesso import ControleAcessoViewSet  # Importa o ViewSet

# Cria um roteador padrão
router = DefaultRouter()

# Registra o endpoint de acessos com o prefixo 'acessos'
router.register(r'acessos', ControleAcessoViewSet)

# Expõe as rotas registradas
urlpatterns = router.urls
