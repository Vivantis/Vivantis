from rest_framework import viewsets
from .models import Manutencao
from .serializers import ManutencaoSerializer

# ViewSet para o modelo Manutencao
# Permite listar, criar, editar e deletar manutenções
class ManutencaoViewSet(viewsets.ModelViewSet):
    queryset = Manutencao.objects.all().order_by('-data_inicio')
    serializer_class = ManutencaoSerializer
