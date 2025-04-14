from rest_framework import viewsets, filters, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Condominio, Unidade, Morador
from .serializers import CondominioSerializer, UnidadeSerializer, MoradorSerializer
from .permissions import get_viewset_permissions  # Certifique-se de importar isso

# ViewSet para o modelo Condominio
class CondominioViewSet(viewsets.ModelViewSet):
    queryset = Condominio.objects.all()
    serializer_class = CondominioSerializer
    permission_classes = get_viewset_permissions('CondominioViewSet')


# ViewSet para o modelo Unidade
class UnidadeViewSet(viewsets.ModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer
    permission_classes = get_viewset_permissions('UnidadeViewSet')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['numero', 'bloco', 'condominio']


# ViewSet para o modelo Morador
class MoradorViewSet(viewsets.ModelViewSet):
    queryset = Morador.objects.all()
    serializer_class = MoradorSerializer
    permission_classes = get_viewset_permissions('MoradorViewSet')  # Usa as permissões definidas por nome
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['email', 'unidade']
    search_fields = ['nome']

    # 🔒 Endpoint: POST /api/moradores/{id}/aprovar/
    @action(detail=True, methods=['post'], url_path='aprovar')
    def aprovar_morador(self, request, pk=None):
        """
        Ativa o usuário vinculado ao morador (campo .user)
        Requer autenticação com permissão de AdministradorGeral.
        """
        morador = self.get_object()
        if morador.user:
            morador.user.is_active = True
            morador.user.save()
            return Response({'status': 'Morador aprovado com sucesso'}, status=status.HTTP_200_OK)
        return Response({'error': 'Morador não possui usuário vinculado'}, status=status.HTTP_400_BAD_REQUEST)
