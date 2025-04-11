from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone

from .models import AutorizacaoEntrada, Morador
from .serializers import AutorizacaoEntradaSerializer
from .utils_auditoria import registrar_acao  # 👈 Importa a função de auditoria

class AutorizacaoEntradaViewSet(viewsets.ModelViewSet):
    queryset = AutorizacaoEntrada.objects.all()
    serializer_class = AutorizacaoEntradaSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        instancia = serializer.save(criado_por=self.request.user)

        # 📝 Registra criação na auditoria
        registrar_acao(
            usuario=self.request.user,
            tipo_acao='criado',
            entidade='AutorizacaoEntrada',
            objeto_id=instancia.id,
            descricao=f"Solicitação criada para {instancia.nome_visitante} na unidade {instancia.unidade_destino}"
        )

    def perform_update(self, serializer):
        instancia = serializer.instance

        # Bloqueia alterações após resposta
        if instancia.status != 'pendente':
            raise serializers.ValidationError("Essa solicitação já foi respondida.")

        morador = self._morador_logado()

        instancia = serializer.save(
            respondido_por=morador,
            respondido_em=timezone.now()
        )

        # 📝 Registra atualização na auditoria
        registrar_acao(
            usuario=self.request.user,
            tipo_acao='editado',
            entidade='AutorizacaoEntrada',
            objeto_id=instancia.id,
            descricao=f"Solicitação respondida como {instancia.get_status_display()} por {morador.nome if morador else 'Usuário'}"
        )

    def _morador_logado(self):
        from .models import Morador
        try:
            return Morador.objects.get(email=self.request.user.email)
        except Morador.DoesNotExist:
            return None
