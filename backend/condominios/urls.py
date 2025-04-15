from django.urls import path, include
from rest_framework.routers import DefaultRouter

# ─────────────────────────────────────────────────────────────
# 📦 Importação dos ViewSets principais
# ─────────────────────────────────────────────────────────────
from .views import CondominioViewSet, UnidadeViewSet, MoradorViewSet
from .views_prestadores import PrestadorViewSet

# ─────────────────────────────────────────────────────────────
# 🔧 Roteador padrão do Django REST Framework
# ─────────────────────────────────────────────────────────────
router = DefaultRouter()
router.register(r'condominios', CondominioViewSet)
router.register(r'unidades', UnidadeViewSet)
router.register(r'moradores', MoradorViewSet)  # Inclui delegar-voto e aprovar
router.register(r'prestadores', PrestadorViewSet)

# ─────────────────────────────────────────────────────────────
# 🌐 URL padrão da aplicação
# ─────────────────────────────────────────────────────────────
urlpatterns = [
    path('', include(router.urls)),  # Inclui as rotas dos ViewSets registrados
]

# ─────────────────────────────────────────────────────────────
# 📁 Inclusão modular das rotas de cada funcionalidade extra
# ─────────────────────────────────────────────────────────────

from .urls_ocorrencias import urlpatterns as ocorrencias_urls
urlpatterns += ocorrencias_urls

from .urls_visitantes import urlpatterns as visitantes_urls
urlpatterns += visitantes_urls

from .urls_acesso import urlpatterns as acesso_urls
urlpatterns += acesso_urls

from .urls_correspondencias import urlpatterns as correspondencias_urls
urlpatterns += correspondencias_urls

from .urls_reservas import urlpatterns as reservas_urls
urlpatterns += reservas_urls

from .urls_documentos import urlpatterns as documentos_urls
urlpatterns += documentos_urls

from .urls_administradores import urlpatterns as administradores_urls
urlpatterns += administradores_urls

from .urls_avisos import urlpatterns as avisos_urls
urlpatterns += avisos_urls

from .urls_manutencao import urlpatterns as manutencao_urls
urlpatterns += manutencao_urls

from .urls_relatorios import urlpatterns as relatorios_urls
urlpatterns += relatorios_urls

from .urls_cobrancas import urlpatterns as cobrancas_urls
urlpatterns += cobrancas_urls

from .urls_comprovantes import urlpatterns as comprovantes_urls
urlpatterns += comprovantes_urls

from .urls_autorizacoes import urlpatterns as autorizacoes_urls
urlpatterns += autorizacoes_urls

from .urls_auditoria import urlpatterns as auditoria_urls
urlpatterns += auditoria_urls

from .urls_perfil import urlpatterns as perfil_urls
urlpatterns += perfil_urls

from .urls_cadastro_aprovacao import urlpatterns as cadastro_aprovacao_urls
urlpatterns += cadastro_aprovacao_urls
