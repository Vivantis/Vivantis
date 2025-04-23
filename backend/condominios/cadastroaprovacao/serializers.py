# backend/condominios/cadastroaprovacao/serializers.py

from django.contrib.auth.models import User
from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field

class CadastroUsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        # ajuste os campos conforme sua API: username, email, etc.
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        # cria usuário inativo
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            is_active=False
        )
        return user

class AprovarUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_active']
        extra_kwargs = {'is_active': {'read_only': True}}
