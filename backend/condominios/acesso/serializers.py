# 🚪 Controle de Acesso
from rest_framework import serializers
from condominios.models import ControleAcesso

class ControleAcessoSerializer(serializers.ModelSerializer):
    tipo_display = serializers.SerializerMethodField()

    class Meta:
        model = ControleAcesso
        fields = [
            'id', 'tipo', 'tipo_display',
            'morador', 'visitante', 'prestador', 'unidade',
            'data_entrada', 'data_saida', 'observacoes'
        ]

    def get_tipo_display(self, obj):
        return obj.get_tipo_display()
