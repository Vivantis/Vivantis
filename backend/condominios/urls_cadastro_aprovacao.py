from django.urls import path
from .views_cadastro_aprovacao import CadastroUsuarioView, AprovarUsuarioView

urlpatterns = [
    path('cadastro/', CadastroUsuarioView.as_view(), name='cadastro-usuario'),
    path('cadastro/aprovar/<int:pk>/', AprovarUsuarioView.as_view(), name='aprovar-usuario'),
]
