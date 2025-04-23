from rest_framework import serializers
from condominios.avisos.models import Aviso


# 📢 Serializer para o modelo Aviso
class AvisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aviso
        fields = '__all__'
