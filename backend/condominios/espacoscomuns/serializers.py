from rest_framework import serializers
from .models import EspacoComum

class EspacoComumSerializer(serializers.ModelSerializer):
    nome_condominio = serializers.SerializerMethodField()

    class Meta:
        model = EspacoComum
        fields = ['id', 'nome', 'condominio', 'nome_condominio']

    def get_nome_condominio(self, obj):
        return obj.condominio.nome
