from rest_framework import serializers
from condominios.condominio.models import Condominio

# 📦 Condomínio
class CondominioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condominio
        fields = '__all__'
