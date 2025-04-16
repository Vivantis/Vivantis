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
