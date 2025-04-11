from django.contrib import admin
from django.urls import path, include

# ─────────────────────────────────────────────────────────────
# 🔒 Autenticação JWT
# ─────────────────────────────────────────────────────────────
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# ─────────────────────────────────────────────────────────────
# 📄 Documentação da API com Swagger e Redoc
# ─────────────────────────────────────────────────────────────
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

# ─────────────────────────────────────────────────────────────
# 🌐 URLs principais do projeto
# ─────────────────────────────────────────────────────────────
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin padrão do Django
    path('api/', include('condominios.urls')),  # Rotas da aplicação principal
]

# ─────────────────────────────────────────────────────────────
# 🔐 Rotas de autenticação JWT
# ─────────────────────────────────────────────────────────────
urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),       # Geração de token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),      # Renovação de token
]

# ─────────────────────────────────────────────────────────────
# 📘 Rotas da documentação interativa da API
# ─────────────────────────────────────────────────────────────
urlpatterns += [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),                      # Schema OpenAPI
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # Swagger UI
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),         # Redoc
]
