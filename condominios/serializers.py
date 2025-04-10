from rest_framework import serializers
from .models import (
    Condominio,
    Unidade,
    Morador,
    Prestador,
    Ocorrencia,
    Visitante,
    ControleAcesso,
    Correspondencia,
    ReservaEspaco,
    EspacoComum
)

# ─────────────────────────────────────────────────────────────
# Serializer para o modelo Condomínio
# ─────────────────────────────────────────────────────────────
class CondominioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condominio
        fields = '__all__'


# ─────────────────────────────────────────────────────────────
# Serializer para o modelo Unidade
# ─────────────────────────────────────────────────────────────
class UnidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidade
        fields = '__all__'


# ─────────────────────────────────────────────────────────────
# Serializer para o modelo Morador
# ─────────────────────────────────────────────────────────────
class MoradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Morador
        fields = '__all__'


# ─────────────────────────────────────────────────────────────
# Serializer para o modelo Prestador
# ─────────────────────────────────────────────────────────────
class PrestadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestador
        fields = '__all__'


# ─────────────────────────────────────────────────────────────
# Serializer para o modelo Ocorrência
# ─────────────────────────────────────────────────────────────
class OcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = '__all__'


# ─────────────────────────────────────────────────────────────
# Serializer para o modelo Visitante
# ─────────────────────────────────────────────────────────────
class VisitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitante
        fields = '__all__'


# ─────────────────────────────────────────────────────────────
# Serializer para o modelo Controle de Acesso
# ─────────────────────────────────────────────────────────────
class ControleAcessoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControleAcesso
        fields = '__all__'


# ─────────────────────────────────────────────────────────────
# Serializer para o modelo Correspondência
# ─────────────────────────────────────────────────────────────
class CorrespondenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Correspondencia
        fields = '__all__'  # Inclui todos os campos do modelo Correspondencia

 

# ─────────────────────────────────────────────────────────────
# Serializer para o modelo Espaço Comum
# ─────────────────────────────────────────────────────────────
class EspacoComumSerializer(serializers.ModelSerializer):
    class Meta:
        model = EspacoComum
        fields = '__all__'  # Inclui nome e condomínio


# ─────────────────────────────────────────────────────────────
# Serializer para o modelo Reserva de Espaço
# ─────────────────────────────────────────────────────────────
class ReservaEspacoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaEspaco
        fields = '__all__'  # Inclui morador, unidade, espaço, data, horário, etc.
