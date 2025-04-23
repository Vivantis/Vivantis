from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from .serializers import CadastroUsuarioSerializer, AprovarUsuarioSerializer

# 👤 Cadastro de novo usuário (inicialmente inativo)
class CadastroUsuarioView(generics.CreateAPIView):
    """
    Cria um novo User com is_active=False.
    """
    queryset = User.objects.all()
    serializer_class = CadastroUsuarioSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        # Salva o usuário desativado
        serializer.save(is_active=False)


# ✅ Aprovação de usuário (ativa o acesso)
class AprovarUsuarioView(generics.UpdateAPIView):
    """
    Define is_active=True para o User indicado.
    """
    queryset = User.objects.all()
    serializer_class = AprovarUsuarioSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'

    def patch(self, request, *args, **kwargs):
        # Recebe o objeto User
        user = self.get_object()
        # Marca como ativo
        user.is_active = True
        user.save()
        # Retorna os dados atualizados
        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
