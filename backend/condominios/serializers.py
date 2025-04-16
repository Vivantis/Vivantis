from rest_framework import serializers
from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema_field
from .models import (
    Condominio, Unidade, Morador, Prestador, Ocorrencia, Visitante,
    ControleAcesso, Correspondencia, ReservaEspaco, EspacoComum, Documento,
    AdministradorGeral, Aviso, Manutencao, Cobranca, ComprovantePagamento,
    AutorizacaoEntrada, Auditoria, PerfilUsuario
)



























# 🧑‍💻 Perfil de Usuário
class PerfilUsuarioSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = PerfilUsuario
        fields = ['id', 'username', 'email', 'telefone', 'foto', 'bio']


# 👤 Serializer para criação de usuários com senha segura e ativação manual
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_active']
        read_only_fields = ['id', 'is_active']

    def create(self, validated_data):
        is_active = validated_data.get('is_active', False)

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        user.is_active = is_active
        user.save()
        return user


# 📊 Relatório Geral
class RelatorioGeralSerializer(serializers.Serializer):
    total_condominios = serializers.IntegerField()
    total_moradores = serializers.IntegerField()
    total_ocorrencias_abertas = serializers.IntegerField()
    total_visitantes_hoje = serializers.IntegerField()
    reservas_por_espaco = serializers.ListField(
        child=serializers.DictField(
            child=serializers.CharField()
        )
    )
