from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from .models import Ocorrencia  # import relativo para o modelo local

class OcorrenciaSerializer(serializers.ModelSerializer):
    # exibe o label do status
    status_display = serializers.SerializerMethodField()
    # exibe o nome do morador
    morador_nome = serializers.SerializerMethodField()
    # exibe informações da unidade
    unidade_info = serializers.SerializerMethodField()

    class Meta:
        model = Ocorrencia
        fields = [
            'id', 'titulo', 'descricao',
            'status', 'status_display',
            'morador', 'morador_nome',
            'unidade', 'unidade_info',
            'data_registro', 'atualizado_em'
        ]
        read_only_fields = ['data_registro', 'atualizado_em']

    @extend_schema_field(str)
    def get_status_display(self, obj: Ocorrencia) -> str:
        return obj.get_status_display()

    @extend_schema_field(str)
    def get_morador_nome(self, obj: Ocorrencia) -> str:
        return obj.morador.nome if obj.morador else None

    @extend_schema_field(str)
    def get_unidade_info(self, obj: Ocorrencia) -> str:
        return str(obj.unidade) if obj.unidade else None
