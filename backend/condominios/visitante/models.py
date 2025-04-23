from django.db import models
from condominios.unidade.models import Unidade
from condominios.morador.models import Morador

# 👥 Visitante autorizado por um morador
class Visitante(models.Model):
    nome = models.CharField(max_length=100)
    documento = models.CharField(max_length=50)
    data_visita = models.DateTimeField(auto_now_add=True)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, related_name='visitantes')
    morador_responsavel = models.ForeignKey(Morador, on_delete=models.CASCADE, related_name='visitantes_autorizados')

    class Meta:
        verbose_name = "Visitante"
        verbose_name_plural = "Visitantes"
        ordering = ['-data_visita']

    def __str__(self):
        return f"{self.nome} - Unidade {self.unidade}"
