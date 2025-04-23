from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from condominios.morador.models import Morador


class MoradorSerializer(serializers.ModelSerializer):
    nome_completo = serializers.SerializerMethodField()
    pode_votar_display = serializers.SerializerMethodField()

    class Meta:
        model = Morador
        fields = [
            'id',
            'nome',
            'sobrenome',
            'nome_completo',
            'email',
            'unidade',
            'cpf',
            'rg',
            'is_proprietario',
            'is_inquilino',
            'pode_votar',
            'pode_votar_display',
        ]

    @extend_schema_field(str)
    def get_nome_completo(self, obj: Morador) -> str:
        if obj.sobrenome:
            return f"{obj.nome} {obj.sobrenome}"
        return obj.nome

    @extend_schema_field(str)
    def get_pode_votar_display(self, obj: Morador) -> str:
        return "Sim" if obj.pode_votar else "Não"
