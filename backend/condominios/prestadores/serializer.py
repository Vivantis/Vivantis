from rest_framework import serializers
from .models import Prestador

class PrestadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestador
        fields = '__all__'
