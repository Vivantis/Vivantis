from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema

from condominios.serializers import UserSerializer


# ─────────────────────────────────────────────────────────────
# 🔐 1. Cadastro de novo usuário (inativo por padrão)
# Endpoint: POST /api/usuarios/cadastro/
# ─────────────────────────────────────────────────────────────
class CadastroUsuarioView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        """
        Cria um novo usuário com is_active=False, independentemente do payload.
        """
        data = request.data.copy()
        data['is_active'] = False  # Garante que o usuário será inativo

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()


# ─────────────────────────────────────────────────────────────
# ✅ 2. Aprovação de usuário (admin ativa a conta)
# Endpoint: PATCH /api/usuarios/cadastro/aprovar/<id>/
# ─────────────────────────────────────────────────────────────
class AprovarUsuarioView(APIView):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer  # Ajuda na documentação do Swagger

    @extend_schema(responses=UserSerializer)
    def patch(self, request, pk):
        """
        Ativa a conta de um usuário inativo.
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


# ─────────────────────────────────────────────────────────────
# 📋 3. Listagem de usuários pendentes (inativos)
# Endpoint: GET /api/usuarios/cadastro/pendentes/
# ─────────────────────────────────────────────────────────────
class UsuariosPendentesView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return User.objects.filter(is_active=False)
