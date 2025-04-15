# condominios/views_autorizacoes.py

from rest_framework import viewsets, status, serializers
from rest_framework.response import Response
from django.utils import timezone
from django.forms.models import model_to_dict

from .models import AutorizacaoEntrada, Morador
from .serializers import AutorizacaoEntradaSerializer
from .utils_auditoria import registrar_acao
from .permissions import get_viewset_permissions  # 🔐 Importa permissões dinâmicas

# 🗒️ ViewSet para Autorização de Entrada Remota
class AutorizacaoEntradaViewSet(viewsets.ModelViewSet):
    queryset = AutorizacaoEntrada.objects.all()
    serializer_class = AutorizacaoEntradaSerializer
    permission_classes = get_viewset_permissions('AutorizacaoEntradaViewSet')

    def perform_create(self, serializer):
        """
        Ao criar, registra quem criou e salva no histórico de auditoria.
        """
        instance = serializer.save(criado_por=self.request.user)

        registrar_acao(
            usuario=self.request.user,
            tipo_acao='criado',
            instancia=instance,
            descricao=f"Solicitação criada para {instance.nome_visitante} na unidade {instance.unidade_destino}"
        )

    def perform_update(self, serializer):
        """
        Ao atualizar, registra quem respondeu, quando e salva no histórico de auditoria.
        Impede edição se já tiver sido respondida.
        """
        instance = self.get_object()

        if instance.status != 'pendente':
            raise serializers.ValidationError("Essa solicitação já foi respondida.")

        morador = self._morador_logado()
        dados_anteriores = model_to_dict(instance)

        instance = serializer.save(
            respondido_por=morador,
            respondido_em=timezone.now()
        )

        registrar_acao(
            usuario=self.request.user,
            tipo_acao='editado',
            instancia=instance,
            descricao=f"Solicitação respondida como {instance.get_status_display()} por {morador.nome if morador else 'Usuário'}",
            dados_anteriores=dados_anteriores
        )

    def _morador_logado(self):
        """
        Busca o morador logado com base no e-mail do usuário autenticado.
        """
        try:
            return Morador.objects.get(email=self.request.user.email)
        except Morador.DoesNotExist:
            return None
