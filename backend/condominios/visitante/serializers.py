from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from .models import Visitante

# 👥 Visitante
class VisitanteSerializer(serializers.ModelSerializer):
    nome_unidade = serializers.SerializerMethodField()
    morador_nome = serializers.SerializerMethodField()

    class Meta:
        model = Visitante
        fields = [
            'id', 'nome', 'documento', 'data_visita',
            'unidade', 'morador_responsavel',
            'nome_unidade', 'morador_nome',
        ]
        read_only_fields = ['data_visita']

    @extend_schema_field(str)
    def get_nome_unidade(self, obj):
        return str(obj.unidade)

    @extend_schema_field(str)
    def get_morador_nome(self, obj):
        return obj.morador_responsavel.nome
