from rest_framework import viewsets
from .models import AdministradorGeral
from .serializers import AdministradorGeralSerializer

# ViewSet para o modelo Administrador Geral
# Permite CRUD para gestores que acessam múltiplos condomínios
class AdministradorGeralViewSet(viewsets.ModelViewSet):
    queryset = AdministradorGeral.objects.all().order_by('nome')
    serializer_class = AdministradorGeralSerializer
