from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from .serializer import CadastroUsuarioSerializer, AprovarUsuarioSerializer

# 👤 Cadastro de novo usuário (inicialmente inativo)
class CadastroUsuarioView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CadastroUsuarioSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(is_active=False)

# ✅ Aprovação de usuário (ativa o acesso)
class AprovarUsuarioView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = AprovarUsuarioSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'
