from rest_framework.routers import DefaultRouter
from .views_ocorrencias import OcorrenciaViewSet  # Importa o ViewSet de Ocorrências

# Cria um roteador padrão do DRF
router = DefaultRouter()

# Registra a rota de ocorrências com o prefixo 'ocorrencias'
router.register(r'ocorrencias', OcorrenciaViewSet)

# Expõe as URLs geradas pelo roteador
urlpatterns = router.urls
