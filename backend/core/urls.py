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

    # API principal
    path('api/', include('condominios.urls')),

    # Cadastro e aprovação de usuários
    path('api/usuarios/', include('condominios.urls_cadastro_aprovacao')),

    # 🔐 JWT Auth endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # 📘 Documentação Swagger e Redoc
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
