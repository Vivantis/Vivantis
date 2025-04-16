# 👥 Visitante
class Visitante(models.Model):
    nome = models.CharField(max_length=100)
    documento = models.CharField(max_length=50)
    data_visita = models.DateTimeField(auto_now_add=True)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    morador_responsavel = models.ForeignKey(Morador, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - Unidade {self.unidade}"


