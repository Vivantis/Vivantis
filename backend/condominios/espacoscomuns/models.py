from django.db import models
from condominios.condominio.models import Condominio

# 🏛️ Espaços comuns disponíveis para reserva (salão, churrasqueira, etc)
class EspacoComum(models.Model):
    nome = models.CharField(max_length=100)
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} ({self.condominio.nome})"

    class Meta:
        verbose_name = "Espaço Comum"
        verbose_name_plural = "Espaços Comuns"
        ordering = ['nome']
        unique_together = ('nome', 'condominio')  # Evita espaços com mesmo nome no mesmo condomínio
