# condominios/views_autorizacoes.py

from rest_framework import viewsets, status, serializers
from rest_framework.response import Response
from .models import AutorizacaoEntrada, Morador
from .serializers import AutorizacaoEntradaSerializer
from .utils_auditoria import registrar_acao
from .permissions import get_viewset_permissions  # 🔐 Importa permissões dinâmicas
from django.utils import timezone

# ViewSet para o modelo Autorização de Entrada
# Usado para aprovar/recusar visitas remotamente por moradores
class AutorizacaoEntradaViewSet(viewsets.ModelViewSet):
    queryset = AutorizacaoEntrada.objects.all()
    serializer_class = AutorizacaoEntradaSerializer
    permission_classes = get_viewset_permissions('AutorizacaoEntradaViewSet')

    def perform_create(self, serializer):
        """
        Ao criar, registra quem criou e salva auditoria.
        """
        instancia = serializer.save(criado_por=self.request.user)

        # 📝 Registro de criação na auditoria
        registrar_acao(
            usuario=self.request.user,
            tipo_acao='criado',
            entidade='AutorizacaoEntrada',
            objeto_id=instancia.id,
            descricao=f"Solicitação criada para {instancia.nome_visitante} na unidade {instancia.unidade_destino}"
        )

    def perform_update(self, serializer):
        """
        Ao atualizar, registra quem respondeu, quando e salva na auditoria.
        Bloqueia alteração se a solicitação já foi respondida.
        """
        instancia = serializer.instance

        if instancia.status != 'pendente':
            raise serializers.ValidationError("Essa solicitação já foi respondida.")

        morador = self._morador_logado()

        instancia = serializer.save(
            respondido_por=morador,
            respondido_em=timezone.now()
        )

        # 📝 Registro de edição na auditoria
        registrar_acao(
            usuario=self.request.user,
            tipo_acao='editado',
            entidade='AutorizacaoEntrada',
            objeto_id=instancia.id,
            descricao=f"Solicitação respondida como {instancia.get_status_display()} por {morador.nome if morador else 'Usuário'}"
        )

    def _morador_logado(self):
        """
        Busca o morador logado com base no e-mail do usuário autenticado.
        """
        try:
            return Morador.objects.get(email=self.request.user.email)
        except Morador.DoesNotExist:
            return None
