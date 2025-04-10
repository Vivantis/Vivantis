from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count
from django.utils import timezone  # ✅ Import necessário para pegar a data atual corretamente

from .models import Condominio, Morador, Ocorrencia, Visitante, ReservaEspaco

# View para retornar um relatório geral consolidado
class RelatorioGeralAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Requer autenticação JWT

    def get(self, request):
        """
        Retorna estatísticas gerais do sistema para exibição em dashboards ou painéis administrativos.
        """
        data = {
            "total_condominios": Condominio.objects.count(),
            "total_moradores": Morador.objects.count(),
            "total_ocorrencias_abertas": Ocorrencia.objects.filter(status='aberta').count(),
            "total_visitantes_hoje": Visitante.objects.filter(data_visita__date=timezone.now().date()).count(),
            "reservas_por_espaco": ReservaEspaco.objects.values('espaco__nome').annotate(total=Count('id')),
        }

        return Response(data)
