from rest_framework.routers import DefaultRouter
from .views_visitantes import VisitanteViewSet  # Importa o ViewSet de Visitantes

# Cria um roteador padrão do DRF
router = DefaultRouter()

# Registra a rota de visitantes com o prefixo 'visitantes'
router.register(r'visitantes', VisitanteViewSet)

# Expõe as URLs geradas pelo roteador
urlpatterns = router.urls
