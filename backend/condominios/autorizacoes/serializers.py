# ✅ Autorização de Entrada Remota
class AutorizacaoEntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutorizacaoEntrada
        fields = '__all__'
        read_only_fields = [
            'criado_em',         # Data em que foi criada
            'respondido_em',     # Data da resposta
            'respondido_por',    # Morador que respondeu
            'criado_por'         # Usuário da portaria que criou
        ]
