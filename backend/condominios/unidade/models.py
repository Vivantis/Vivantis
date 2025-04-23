from django.db import models
from condominios.condominio.models import Condominio

# 🏠 Unidade residencial dentro de um condomínio
class Unidade(models.Model):
    numero = models.CharField(max_length=10)
    bloco = models.CharField(max_length=10, null=True, blank=True)
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='unidades')

    class Meta:
        unique_together = ('numero', 'bloco', 'condominio')
        verbose_name = "Unidade"
        verbose_name_plural = "Unidades"
        ordering = ['condominio', 'bloco', 'numero']

    def __str__(self):
        bloco_info = f" - Bloco {self.bloco}" if self.bloco else ""
        return f"Apto {self.numero}{bloco_info} - {self.condominio.nome}"
