# condominios/views_prestadores.py

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Prestador
from .serializers import PrestadorSerializer
from .permissions import get_viewset_permissions


# ─────────────────────────────────────────────────────────────
# 👷 ViewSet para Prestadores de Serviço
# Permite que administradores registrem e gerenciem prestadores
# ─────────────────────────────────────────────────────────────
class PrestadorViewSet(viewsets.ModelViewSet):
    queryset = Prestador.objects.all()
    serializer_class = PrestadorSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nome']  # ⬅️ Aqui definimos que só será possível buscar por 'nome'
    ordering_fields = ['nome']
