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