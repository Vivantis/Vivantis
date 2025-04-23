from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from .models import Documento

class DocumentoSerializer(serializers.ModelSerializer):
    # Campo extra para exibir o label do tipo
    tipo_display = serializers.SerializerMethodField()

    @extend_schema_field(serializers.CharField())
    def get_tipo_display(self, obj):
        return obj.get_tipo_display()

    class Meta:
        model = Documento
        # Use '__all__' para incluir todos os campos do modelo
        # e o SerializerMethodField 'tipo_display' declarado acima
        fields = '__all__'
