from rest_framework import viewsets
from .models import EspacoComum, ReservaEspaco
from .serializers import EspacoComumSerializer, ReservaEspacoSerializer

# ViewSet para espaços comuns
class EspacoComumViewSet(viewsets.ModelViewSet):
    queryset = EspacoComum.objects.all()
    serializer_class = EspacoComumSerializer


# ViewSet para reservas de espaços
class ReservaEspacoViewSet(viewsets.ModelViewSet):
    queryset = ReservaEspaco.objects.all().order_by('-data_reserva', '-horario_inicio')
    serializer_class = ReservaEspacoSerializer
