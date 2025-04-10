# condominios/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CondominioViewSet, UnidadeViewSet, MoradorViewSet
from .views_prestadores import PrestadorViewSet  # Importa o ViewSet de prestadores

# Cria um roteador padrão do DRF
router = DefaultRouter()

# Registra os módulos no roteador
router.register(r'condominios', CondominioViewSet)
router.register(r'unidades', UnidadeViewSet)
router.register(r'moradores', MoradorViewSet)
router.register(r'prestadores', PrestadorViewSet)  # Novo módulo adicionado aqui

# Define as rotas da aplicação condominios
urlpatterns = [
    path('', include(router.urls)),  # Inclui todas as rotas registradas acima
]
