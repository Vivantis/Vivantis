from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from .models import Documento

class DocumentoSerializer(serializers.ModelSerializer):
    tipo_display = serializers.SerializerMethodField()

    class Meta:
        model = Documento
        fields = '__all__' + ['tipo_display']  # inclui display adicional

    @extend_schema_field(str)
    def get_tipo_display(self, obj):
        return obj.get_tipo_display()
