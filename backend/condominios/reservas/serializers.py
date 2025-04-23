from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from .models import ReservaEspaco

class ReservaEspacoSerializer(serializers.ModelSerializer):
    # Exemplo de campo extra, se quiser mostrar label de status
    status_display = serializers.SerializerMethodField()

    @extend_schema_field(serializers.CharField())
    def get_status_display(self, obj):
        return obj.get_status_display()

    class Meta:
        model = ReservaEspaco
        fields = '__all__'
