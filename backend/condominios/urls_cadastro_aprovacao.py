from django.urls import path
from .views_cadastro_aprovacao import CadastroUsuarioView, AprovarUsuarioView

urlpatterns = [
    # 🔹 Endpoint público para cadastro de novo usuário (is_active=False)
    path('cadastro/', CadastroUsuarioView.as_view(), name='cadastro-usuario'),

    # 🔒 Endpoint restrito ao admin para aprovar um usuário (ativa o is_active=True)
    path('cadastro/aprovar/<int:pk>/', AprovarUsuarioView.as_view(), name='aprovar-usuario'),
]
