from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound

from condominios.serializers import UserSerializer

# View de Cadastro de Usuário (não ativa o usuário automaticamente)
class CadastroUsuarioView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        """
        Sobrescreve o método create para garantir que todo novo usuário
        seja criado com is_active=False, mesmo que venha no payload.
        """
        # Faz uma cópia dos dados enviados e força is_active=False
        data = request.data.copy()
        data['is_active'] = False

        # Valida e salva o usuário
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        # Criação do usuário inativo
        serializer.save()

# View para um administrador aprovar um usuário (ativar)
class AprovarUsuarioView(APIView):
    permission_classes = [IsAdminUser]

    def patch(self, request, pk):
        """
        Permite que um superusuário aprove um usuário pendente,
        ativando sua conta (is_active=True)
        """
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound("Usuário não encontrado.")

        if user.is_active:
            return Response({"detail": "Usuário já está ativo."}, status=status.HTTP_400_BAD_REQUEST)

        user.is_active = True
        user.save()
        return Response({"detail": "Usuário aprovado com sucesso."}, status=status.HTTP_200_OK)
