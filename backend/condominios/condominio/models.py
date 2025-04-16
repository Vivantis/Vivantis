# 🏢 Modelo que representa um Condomínio
class Condominio(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.TextField()
    cidade = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=2, blank=True, null=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
