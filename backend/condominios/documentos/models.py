# 📂 Documentos
class Documento(models.Model):
    TIPO_CHOICES = [
        ('regulamento', 'Regulamento Interno'),
        ('ata', 'Ata de Reunião'),
        ('edital', 'Edital'),
        ('boleto', 'Boleto'),
        ('outro', 'Outro'),
    ]

    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='outro')
    arquivo = models.FileField(upload_to='documentos/')  # Caminho onde os arquivos serão salvos
    visivel_para_moradores = models.BooleanField(default=True)
    data_envio = models.DateTimeField(auto_now_add=True)
    enviado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} - {self.get_tipo_display()}"
