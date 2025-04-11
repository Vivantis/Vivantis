from django.urls import path
from .views_perfil import MeuPerfilView

urlpatterns = [
    path('perfil/', MeuPerfilView.as_view(), name='meu-perfil'),
]
