# 🏛️ Espaços Comuns
class EspacoComum(models.Model):
    nome = models.CharField(max_length=100)
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} ({self.condominio.nome})"
