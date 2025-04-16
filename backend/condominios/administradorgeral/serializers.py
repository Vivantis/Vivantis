
# 👨‍💼 Administrador Geral
class AdministradorGeralSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdministradorGeral
        fields = '__all__'
        read_only_fields = ['criado_em', 'user']

