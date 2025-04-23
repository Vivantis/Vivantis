from django.db import models
from condominios.morador.models import Morador
from condominios.unidade.models import Unidade

# 📦 Correspondência recebida na portaria
class Correspondencia(models.Model):
    descricao = models.CharField(max_length=200)
    morador = models.ForeignKey(Morador, on_delete=models.CASCADE)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    data_recebimento = models.DateTimeField(auto_now_add=True)
    data_retirada = models.DateTimeField(null=True, blank=True)
    entregue_por = models.CharField(max_length=100, blank=True)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.descricao} - {self.morador.nome}"

    class Meta:
        verbose_name = "Correspondência"
        verbose_name_plural = "Correspondências"
        ordering = ['-data_recebimento']
