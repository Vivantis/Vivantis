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
    EspacoComum,
    Documento,
    AdministradorGeral,
    Aviso,
    Manutencao,
    Cobranca,
    ComprovantePagamento,
    AutorizacaoEntrada,
    Auditoria,
    PerfilUsuario
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

# ─────────────────────────────────────────────────────────────
# Serializer para o modelo Documento
# ─────────────────────────────────────────────────────────────
class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = '__all__'  # Inclui todos os campos do modelo Documento



# ─────────────────────────────────────────────────────────────
# Serializer para o modelo Administrador Geral
# ─────────────────────────────────────────────────────────────
class AdministradorGeralSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdministradorGeral
        fields = '__all__'  # Inclui user, nome, telefone, etc.


# ─────────────────────────────────────────────────────────────
# Serializer para o modelo Aviso
# ─────────────────────────────────────────────────────────────
class AvisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aviso
        fields = '__all__'  # Inclui todos os campos do modelo Aviso

# ─────────────────────────────────────────────────────────────
# Serializer para o modelo Manutencao
# ─────────────────────────────────────────────────────────────
class ManutencaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manutencao
        fields = '__all__'  # Inclui todos os campos do modelo Manutencao 

# Serializer para o modelo de cobrança
# Converte os dados de cobrança entre JSON e modelo
class CobrancaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cobranca
        fields = '__all__'

# Serializer para o modelo ComprovantePagamento
# Responsável por converter os dados entre JSON e modelo
class ComprovantePagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComprovantePagamento
        fields = '__all__'


class AutorizacaoEntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutorizacaoEntrada
        fields = '__all__'  # Inclui todos os campos do modelo
        read_only_fields = ['criado_em', 'respondido_em', 'respondido_por', 'criado_por']


class AuditoriaSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField()  # Mostra o nome do usuário

    class Meta:
        model = Auditoria
        fields = '__all__'
        read_only_fields = ['usuario', 'data']  # Nenhum campo é editável manualmente

    # 🔄 Serializer para o perfil do usuário
class PerfilUsuarioSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = PerfilUsuario
        fields = ['id', 'username', 'email', 'telefone', 'foto', 'bio']