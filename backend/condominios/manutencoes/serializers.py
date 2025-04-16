from drf_spectacular.utils import extend_schema_field

class ManutencaoSerializer(serializers.ModelSerializer):
    status_display = serializers.SerializerMethodField()

    class Meta:
        model = Manutencao
        fields = '__all__'

    @extend_schema_field(str)
    def get_status_display(self, obj):
        return obj.get_status_display()
