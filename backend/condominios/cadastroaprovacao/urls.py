from django.urls import path
from .views import CadastroUsuarioView, AprovarUsuarioView

urlpatterns = [
    path('cadastro/', CadastroUsuarioView.as_view(), name='cadastro-usuario'),
    path('aprovar/<int:pk>/', AprovarUsuarioView.as_view(), name='aprovar-usuario'),
]
