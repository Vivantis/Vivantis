from django.urls import path, include
from rest_framework.routers import DefaultRouter

# ───── ViewSets principais ─────
from .views import CondominioViewSet, UnidadeViewSet, MoradorViewSet
from .views_prestadores import PrestadorViewSet

# ───── Roteador padrão do Django REST Framework ─────
router = DefaultRouter()

# ───── Registro de rotas principais ─────
router.register(r'condominios', CondominioViewSet)
router.register(r'unidades', UnidadeViewSet)
router.register(r'moradores', MoradorViewSet)
router.register(r'prestadores', PrestadorViewSet)

# ───── URLs da aplicação 'condominios' ─────
urlpatterns = [
    path('', include(router.urls)),  # Inclui rotas principais registradas acima
]

# ───── URLs modulares adicionais (ocorrências e visitantes) ─────
from .urls_ocorrencias import urlpatterns as ocorrencias_urls
urlpatterns += ocorrencias_urls

from .urls_visitantes import urlpatterns as visitantes_urls
urlpatterns += visitantes_urls


from .urls_acesso import urlpatterns as acesso_urls
urlpatterns += acesso_urls  # Adiciona as rotas do módulo Controle de Acesso

from .urls_correspondencias import urlpatterns as correspondencias_urls
urlpatterns += correspondencias_urls  # Adiciona as rotas de correspondências

from .urls_reservas import urlpatterns as reservas_urls
urlpatterns += reservas_urls  # Adiciona as rotas de espaços e reservas

from .urls_documentos import urlpatterns as documentos_urls
urlpatterns += documentos_urls  # Adiciona as rotas de documentos

from .urls_administradores import urlpatterns as administradores_urls
urlpatterns += administradores_urls  # Adiciona as rotas de administradores gerais

from .urls_avisos import urlpatterns as avisos_urls
urlpatterns += avisos_urls  # Adiciona as rotas de avisos

from .urls_manutencao import urlpatterns as manutencao_urls
urlpatterns += manutencao_urls  # Adiciona as rotas de manutenções]

from .urls_relatorios import urlpatterns as relatorios_urls
urlpatterns += relatorios_urls

from .urls_cobrancas import urlpatterns as cobrancas_urls
urlpatterns += cobrancas_urls

from .urls_comprovantes import urlpatterns as comprovantes_urls
urlpatterns += comprovantes_urls


