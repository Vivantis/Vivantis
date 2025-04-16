class PrestadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestador
        fields = '__all__'
        read_only_fields = ['id']  # Exemplo
