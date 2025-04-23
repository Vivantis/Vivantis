from rest_framework import serializers
from .models import PerfilUsuario
from django.contrib.auth.models import User

class PerfilUsuarioSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = PerfilUsuario
        fields = ['id', 'user', 'username', 'email', 'telefone', 'foto', 'bio']
