from rest_framework import serializers
from condominios.models import Unidade


class UnidadeSerializer(serializers.ModelSerializer):
    condominio_nome = serializers.CharField(source='condominio.nome', read_only=True)

    class Meta:
        model = Unidade
        fields = [
            'id',
            'numero',
            'bloco',
            'condominio',
            'condominio_nome'
        ]
