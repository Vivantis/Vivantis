from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from .models import Correspondencia

# 📦 Correspondência
class CorrespondenciaSerializer(serializers.ModelSerializer):
    nome_morador = serializers.SerializerMethodField()
    retirada_display = serializers.SerializerMethodField()

    class Meta:
        model = Correspondencia
        fields = [
            'id', 'morador', 'unidade', 'descricao', 'entregue_por',
            'data_recebimento', 'data_retirada', 'observacoes',
            'nome_morador', 'retirada_display'
        ]

    @extend_schema_field(str)
    def get_nome_morador(self, obj):
        return obj.morador.nome

    @extend_schema_field(str)
    def get_retirada_display(self, obj):
        return "Retirada" if obj.data_retirada else "Pendente"
