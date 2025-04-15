from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from django.utils import timezone
from drf_spectacular.utils import extend_schema

from .models import Condominio, Morador, Ocorrencia, Visitante, ReservaEspaco
from .permissions import get_viewset_permissions
from .serializers import RelatorioGeralSerializer

# ─────────────────────────────────────────────────────────────
# 📊 APIView para Relatório Geral do Sistema
# Retorna estatísticas agregadas para dashboards administrativos
# ─────────────────────────────────────────────────────────────
class RelatorioGeralAPIView(APIView):
    permission_classes = get_viewset_permissions('RelatorioViewSet')

    @extend_schema(
        responses=RelatorioGeralSerializer,
        description="Retorna contagens e estatísticas agregadas do sistema"
    )
    def get(self, request):
        """
        Retorna estatísticas como total de moradores, visitantes hoje,
        ocorrências abertas e uso dos espaços.
        """
        reservas_agrupadas = ReservaEspaco.objects.values('espaco__nome').annotate(total=Count('id'))

        data = {
            "total_condominios": Condominio.objects.count(),
            "total_moradores": Morador.objects.count(),
            "total_ocorrencias_abertas": Ocorrencia.objects.filter(status='aberta').count(),
            "total_visitantes_hoje": Visitante.objects.filter(data_visita__date=timezone.now().date()).count(),
            "reservas_por_espaco": list(reservas_agrupadas),
        }
        return Response(data)
