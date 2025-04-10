from rest_framework import serializers
from .models import Condominio, Unidade, Morador

# Serializer para o modelo Condominio
class CondominioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condominio
        fields = '__all__'  # inclui todos os campos do modelo

# Serializer para o modelo Unidade
class UnidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidade
        fields = '__all__'

# Serializer para o modelo Morador
class MoradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Morador
        fields = '__all__'
