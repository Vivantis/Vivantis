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
router.register(r'moradores', MoradorViewSet)
router.register(r'prestadores', PrestadorViewSet)

# ─────────────────────────────────────────────────────────────
# 🌐 URL padrão da aplicação
# ─────────────────────────────────────────────────────────────
urlpatterns = [
    path('', include(router.urls)),  # Inclui as rotas dos ViewSets principais
]

# ─────────────────────────────────────────────────────────────
# 📁 Inclusão modular das rotas de cada funcionalidade
# ─────────────────────────────────────────────────────────────

# Ocorrências
from .urls_ocorrencias import urlpatterns as ocorrencias_urls
urlpatterns += ocorrencias_urls

# Visitantes
from .urls_visitantes import urlpatterns as visitantes_urls
urlpatterns += visitantes_urls

# Controle de Acesso
from .urls_acesso import urlpatterns as acesso_urls
urlpatterns += acesso_urls

# Correspondências
from .urls_correspondencias import urlpatterns as correspondencias_urls
urlpatterns += correspondencias_urls

# Espaços e Reservas
from .urls_reservas import urlpatterns as reservas_urls
urlpatterns += reservas_urls

# Documentos
from .urls_documentos import urlpatterns as documentos_urls
urlpatterns += documentos_urls

# Administradores Gerais
from .urls_administradores import urlpatterns as administradores_urls
urlpatterns += administradores_urls

# Avisos e Comunicados
from .urls_avisos import urlpatterns as avisos_urls
urlpatterns += avisos_urls

# Manutenções
from .urls_manutencao import urlpatterns as manutencao_urls
urlpatterns += manutencao_urls

# Relatórios
from .urls_relatorios import urlpatterns as relatorios_urls
urlpatterns += relatorios_urls

# Cobranças Financeiras
from .urls_cobrancas import urlpatterns as cobrancas_urls
urlpatterns += cobrancas_urls

# Comprovantes de Pagamento
from .urls_comprovantes import urlpatterns as comprovantes_urls
urlpatterns += comprovantes_urls

# Autorizações de Entrada Remota
from .urls_autorizacoes import urlpatterns as autorizacoes_urls
urlpatterns += autorizacoes_urls

# Auditoria
from .urls_auditoria import urlpatterns as auditoria_urls
urlpatterns += auditoria_urls

# Perfil do Usuário
from .urls_perfil import urlpatterns as perfil_urls
urlpatterns += perfil_urls

from .urls_cadastro_aprovacao import urlpatterns as cadastro_aprovacao_urls
urlpatterns += cadastro_aprovacao_urls
