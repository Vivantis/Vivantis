from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone

from .models import AutorizacaoEntrada, Morador
from .serializers import AutorizacaoEntradaSerializer

class AutorizacaoEntradaViewSet(viewsets.ModelViewSet):
    queryset = AutorizacaoEntrada.objects.all()
    serializer_class = AutorizacaoEntradaSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Ao criar uma solicitação, registra o usuário (porteiro/admin)
        serializer.save(criado_por=self.request.user)

    def perform_update(self, serializer):
        instancia = serializer.instance

        # Só permite atualizar se ainda estiver pendente
        if instancia.status != 'pendente':
            raise serializers.ValidationError("Essa solicitação já foi respondida.")

        # Define quem respondeu e quando
        serializer.save(
            respondido_por=self._morador_logado(),
            respondido_em=timezone.now()
        )

    def _morador_logado(self):
        try:
            return Morador.objects.get(email=self.request.user.email)
        except Morador.DoesNotExist:
            return None
