from rest_framework import viewsets
from .models import ControleAcesso
from .serializers import ControleAcessoSerializer

# ViewSet para o modelo Controle de Acesso
# Permite registrar entradas e saídas via API
class ControleAcessoViewSet(viewsets.ModelViewSet):
    queryset = ControleAcesso.objects.all().order_by('-data_entrada')
    serializer_class = ControleAcessoSerializer
