from django.db import models
from rest_framework import viewsets


# 🏢 Modelo que representa um Condomínio
class Condominio(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.TextField()
    cidade = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=2, blank=True, null=True)  # Ex: SP, RJ
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Condomínio"
        verbose_name_plural = "Condomínios"
        ordering = ['nome']
