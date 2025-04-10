from rest_framework import viewsets
from .models import Aviso
from .serializers import AvisoSerializer

# ViewSet para o modelo Aviso
# Permite listar, criar, editar e deletar comunicados
class AvisoViewSet(viewsets.ModelViewSet):
    queryset = Aviso.objects.all().order_by('-criado_em')
    serializer_class = AvisoSerializer
