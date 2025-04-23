from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from .models import ComprovantePagamento

class ComprovantePagamentoSerializer(serializers.ModelSerializer):
    # Campo extra para exibir o label de 'validado'
    validado_display = serializers.SerializerMethodField()

    @extend_schema_field(serializers.CharField())
    def get_validado_display(self, obj):
        return obj.get_validado_display()

    class Meta:
        model = ComprovantePagamento
        fields = '__all__'
