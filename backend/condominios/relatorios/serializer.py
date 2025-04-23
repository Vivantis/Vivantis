from rest_framework import serializers
from .models import Relatorio

class RelatorioSerializer(serializers.ModelSerializer):
    gerado_por_nome = serializers.CharField(source='gerado_por.username', read_only=True)

    class Meta:
        model = Relatorio
        fields = ['id', 'titulo', 'tipo', 'gerado_por', 'gerado_por_nome', 'data_geracao', 'arquivo', 'observacoes']
        read_only_fields = ['gerado_por', 'data_geracao']
