from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    Condominio, Unidade, Morador, Prestador, Ocorrencia, Visitante,
    ControleAcesso, Correspondencia, ReservaEspaco, EspacoComum, Documento,
    AdministradorGeral, Aviso, Manutencao, Cobranca, ComprovantePagamento,
    AutorizacaoEntrada, Auditoria, PerfilUsuario
)

# ─────────────────────────────────────────────────────────────
# 🌐 Serializers: responsáveis por transformar os dados entre JSON <-> Modelos
# ─────────────────────────────────────────────────────────────

# 📦 Condomínio
class CondominioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condominio
        fields = '__all__'


# 🏠 Unidade
class UnidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidade
        fields = '__all__'


# 👤 Morador
class MoradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Morador
        fields = '__all__'


# 🛠️ Prestador
class PrestadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestador
        fields = '__all__'


# 📢 Ocorrência
class OcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = '__all__'


# 👥 Visitante
class VisitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitante
        fields = '__all__'


# 🚪 Controle de Acesso
class ControleAcessoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControleAcesso
        fields = '__all__'


# 📦 Correspondência
class CorrespondenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Correspondencia
        fields = '__all__'


# 🧱 Espaço Comum
class EspacoComumSerializer(serializers.ModelSerializer):
    class Meta:
        model = EspacoComum
        fields = '__all__'


# 📅 Reserva de Espaços
class ReservaEspacoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaEspaco
        fields = '__all__'


# 📂 Documentos
class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = '__all__'


# 👨‍💼 Administrador Geral
class AdministradorGeralSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdministradorGeral
        fields = '__all__'


# 🔔 Avisos
class AvisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aviso
        fields = '__all__'


# 🔧 Manutenção
class ManutencaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manutencao
        fields = '__all__'


# 💰 Cobrança
class CobrancaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cobranca
        fields = '__all__'


# 📎 Comprovante de Pagamento
class ComprovantePagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComprovantePagamento
        fields = '__all__'


# ✅ Autorização de Entrada Remota
class AutorizacaoEntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutorizacaoEntrada
        fields = '__all__'
        read_only_fields = ['criado_em', 'respondido_em', 'respondido_por', 'criado_por']


# 📋 Auditoria de Ações
class AuditoriaSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField()  # Exibe o nome do usuário

    class Meta:
        model = Auditoria
        fields = '__all__'
        read_only_fields = ['usuario', 'data']  # Campos protegidos


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
        """
        Cria o usuário com hash da senha e respeita o valor de is_active (default=False).
        """
        is_active = validated_data.get('is_active', False)

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        user.is_active = is_active
        user.save()
        return user
