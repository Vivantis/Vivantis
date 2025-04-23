from django.contrib.auth.models import User
from rest_framework import serializers

class CadastroUsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        user.is_active = False
        user.save()
        return user


class AprovarUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['is_active']
