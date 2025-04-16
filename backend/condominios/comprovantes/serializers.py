from drf_spectacular.utils import extend_schema_field

class ComprovantePagamentoSerializer(serializers.ModelSerializer):
    nome_morador = serializers.SerializerMethodField()
    nome_cobranca = serializers.SerializerMethodField()

    class Meta:
        model = ComprovantePagamento
        fields = [
            'id', 'morador', 'cobranca', 'arquivo', 'comentario',
            'data_envio', 'validado', 'validado_por',
            'nome_morador', 'nome_cobranca'
        ]

    @extend_schema_field(str)
    def get_nome_morador(self, obj):
        return obj.morador.nome if obj.morador else None

    @extend_schema_field(str)
    def get_nome_cobranca(self, obj):
        return str(obj.cobranca) if obj.cobranca else None
