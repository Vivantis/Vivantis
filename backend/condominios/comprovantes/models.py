from django.db import models
from django.contrib.auth.models import User
from condominios.cobrancas.models import Cobranca
from condominios.morador.models import Morador

# 📋 Comprovantes de pagamento enviados pelos moradores
class ComprovantePagamento(models.Model):
    cobranca = models.ForeignKey(
        Cobranca,
        on_delete=models.CASCADE,
        related_name='comprovantes'
    )

    morador = models.ForeignKey(
        Morador,
        on_delete=models.CASCADE,
        related_name='comprovantes_pagamento'
    )

    arquivo = models.FileField(upload_to='comprovantes/')
    comentario = models.TextField(blank=True)

    data_envio = models.DateTimeField(auto_now_add=True)

    validado = models.BooleanField(default=False)

    validado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='comprovantes_validados'
    )

    def __str__(self):
        return f"Comprovante de {self.morador.nome} - {self.cobranca}"

    class Meta:
        verbose_name = "Comprovante de Pagamento"
        verbose_name_plural = "Comprovantes de Pagamento"
        ordering = ['-data_envio']
