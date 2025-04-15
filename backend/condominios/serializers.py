from rest_framework import serializers
from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema_field
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
    nome_completo = serializers.SerializerMethodField()
    pode_votar_display = serializers.SerializerMethodField()

    class Meta:
        model = Morador
        fields = [
            'id', 'nome', 'email', 'unidade',
            'cpf', 'rg', 'nome_completo',
            'is_proprietario', 'is_inquilino', 'pode_votar', 'pode_votar_display'
        ]

    @extend_schema_field(str)
    def get_nome_completo(self, obj: Morador) -> str:
        return obj.nome

    @extend_schema_field(str)
    def get_pode_votar_display(self, obj: Morador) -> str:
        return "Sim" if obj.pode_votar else "Não"


# 🛠️ Prestador
class PrestadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestador
        fields = '__all__'


# 📢 Ocorrência
class OcorrenciaSerializer(serializers.ModelSerializer):
    status_display = serializers.SerializerMethodField()

    class Meta:
        model = Ocorrencia
        fields = [
            'id', 'titulo', 'morador', 'unidade', 'descricao',
            'status', 'atualizado_em', 'status_display'
        ]

    @extend_schema_field(str)
    def get_status_display(self, obj: Ocorrencia) -> str:
        return obj.get_status_display()



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
# 📦 Correspondência
class CorrespondenciaSerializer(serializers.ModelSerializer):
    nome_morador = serializers.SerializerMethodField()
    retirada_display = serializers.SerializerMethodField()

    class Meta:
        model = Correspondencia
        fields = [
            'id', 'morador', 'unidade', 'descricao', 'entregue_por',
            'data_recebimento', 'data_retirada', 'observacoes',
            'nome_morador', 'retirada_display'
        ]

    @extend_schema_field(str)
    def get_nome_morador(self, obj: Correspondencia) -> str:
        return obj.morador.nome

    @extend_schema_field(str)
    def get_retirada_display(self, obj: Correspondencia) -> str:
        return "Retirada" if obj.data_retirada else "Pendente"



# 🧱 Espaço Comum
class EspacoComumSerializer(serializers.ModelSerializer):
    class Meta:
        model = EspacoComum
        fields = '__all__'


# 📅 Reserva de Espaços
class ReservaEspacoSerializer(serializers.ModelSerializer):
    espaco_nome = serializers.SerializerMethodField()
    status_display = serializers.SerializerMethodField()

    class Meta:
        model = ReservaEspaco
        fields = [
            'id', 'espaco', 'morador', 'unidade', 'data', 'horario_inicio',
            'horario_fim', 'status', 'observacoes',
            'espaco_nome', 'status_display'
        ]

    @extend_schema_field(str)
    def get_espaco_nome(self, obj: ReservaEspaco) -> str:
        return obj.espaco.nome if obj.espaco else None

    @extend_schema_field(str)
    def get_status_display(self, obj: ReservaEspaco) -> str:
        return obj.get_status_display()


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
    usuario_nome = serializers.SerializerMethodField()
    data_formatada = serializers.SerializerMethodField()

    class Meta:
        model = Auditoria
        fields = [
            'id',
            'usuario', 'usuario_nome',
            'tipo_acao', 'entidade', 'objeto_id',
            'descricao', 'dados_anteriores', 'dados_novos',
            'data', 'data_formatada'
        ]
        read_only_fields = ['usuario', 'data']

    @extend_schema_field(str)
    def get_usuario_nome(self, obj):
        return obj.usuario.get_full_name() if obj.usuario else "Sistema"

    @extend_schema_field(str)
    def get_data_formatada(self, obj):
        return obj.data.strftime('%d/%m/%Y %H:%M')


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
