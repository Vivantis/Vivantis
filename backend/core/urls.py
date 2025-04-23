from django.contrib import admin
from django.urls import path, include

# 🔒 Autenticação via JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# 📘 Documentação da API (Swagger e Redoc)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    # Admin do Django
    path('admin/', admin.site.urls),

    # 🌐 API modularizada por domínio
    path('api/condominios/', include('condominios.condominio.urls')),
    path('api/unidades/', include('condominios.unidade.urls')),
    path('api/moradores/', include('condominios.morador.urls')),
    path('api/prestadores/', include('condominios.prestadores.urls')),
    path('api/avisos/', include('condominios.avisos.urls')),
    path('api/documentos/', include('condominios.documentos.urls')),
    path('api/ocorrencias/', include('condominios.ocorrencia.urls')),
    path('api/visitantes/', include('condominios.visitante.urls')),
    path('api/controle-acesso/', include('condominios.acesso.urls')),
    path('api/correspondencias/', include('condominios.correspondencia.urls')),
    path('api/reservas/', include('condominios.reservas.urls')),
    path('api/comprovantes/', include('condominios.comprovantes.urls')),
    path('api/cobrancas/', include('condominios.cobrancas.urls')),
    path('api/usuarios/', include('condominios.cadastroaprovacao.urls')),
    path('api/auditoria/', include('condominios.auditoria.urls')),
    path('api/relatorios/', include('condominios.relatorios.urls')),
    path('api/perfil/', include('condominios.perfil.urls')),

    # 🔐 JWT Auth endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # 📘 Documentação Swagger e Redoc
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
