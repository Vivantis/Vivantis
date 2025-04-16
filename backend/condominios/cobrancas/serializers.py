from rest_framework import serializers
from .models import Cobranca

class CobrancaSerializer(serializers.ModelSerializer):
    unidade_nome = serializers.SerializerMethodField()
    morador_nome = serializers.SerializerMethodField()
    status_display = serializers.SerializerMethodField()

    class Meta:
        model = Cobranca
        fields = [
            'id', 'unidade', 'morador', 'tipo', 'descricao',
            'valor', 'vencimento', 'status',
            'criado_em', 'atualizado_em',
            'unidade_nome', 'morador_nome', 'status_display'
        ]

    def get_unidade_nome(self, obj):
        return str(obj.unidade) if obj.unidade else None

    def get_morador_nome(self, obj):
        return obj.morador.nome if obj.morador else None

    def get_status_display(self, obj):
        return obj.get_status_display()
