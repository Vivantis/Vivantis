# 🏠 Unidade
class Unidade(models.Model):
    numero = models.CharField(max_length=10)
    bloco = models.CharField(max_length=10, null=True, blank=True)
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE)

    def __str__(self):
        return f"Apto {self.numero} - {self.condominio.nome}"

class Meta:
        unique_together = ('numero', 'bloco', 'condominio')


