# backend/condominios/acesso/serializers.py

from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from .models import ControleAcesso  # Import relativo ao modelo local

class ControleAcessoSerializer(serializers.ModelSerializer):
    # Campo extra para exibir o label de tipo
    tipo_display = serializers.SerializerMethodField()

    @extend_schema_field(serializers.CharField())
    def get_tipo_display(self, obj):
        return obj.get_tipo_display()

    class Meta:
        model = ControleAcesso
        fields = [
            'id', 'tipo', 'tipo_display',
            'morador', 'visitante', 'prestador',
            'unidade', 'data_entrada',
            'data_saida', 'observacoes'
        ]
