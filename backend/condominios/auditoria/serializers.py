from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from .models import Auditoria

class AuditoriaSerializer(serializers.ModelSerializer):
    # Exemplo de campo extra: usuário que realizou a ação
    usuario_display = serializers.SerializerMethodField()

    @extend_schema_field(serializers.CharField())
    def get_usuario_display(self, obj):
        return str(obj.usuario)  # ou outro atributo de display

    class Meta:
        model = Auditoria
        fields = '__all__'
