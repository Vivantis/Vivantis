from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Documento
from .serializers import DocumentoSerializer
from .permissions import get_viewset_permissions

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all().order_by('-data_envio')  # Mostra os mais recentes primeiro
    serializer_class = DocumentoSerializer
    permission_classes = get_viewset_permissions('DocumentoViewSet')  # 🔐 Permissões específicas

    # 🔍 Suporte a filtros, ordenação e busca via query params
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['tipo', 'condominio', 'visivel_para_moradores']  # Ex: ?tipo=ata&visivel_para_moradores=True
    ordering_fields = ['data_envio', 'titulo']  # Ex: ?ordering=-data_envio
    search_fields = ['titulo']  # Ex: ?search=assembleia
