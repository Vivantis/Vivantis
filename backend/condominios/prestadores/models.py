
# 🚰 Prestador
class Prestador(models.Model):
    nome = models.CharField(max_length=100)
    tipo_servico = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
