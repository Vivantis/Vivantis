from django.db import models
from django.contrib.auth.models import User
from condominios.condominio.models import Condominio

# 🔔 Avisos e Comunicados do Condomínio
class Aviso(models.Model):
    titulo = models.CharField(max_length=150)
    mensagem = models.TextField()

    criado_em = models.DateTimeField(auto_now_add=True)
    expira_em = models.DateTimeField(null=True, blank=True)

    condominio = models.ForeignKey(
        Condominio,
        on_delete=models.CASCADE,
        related_name='avisos'
    )

    publicado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='avisos_publicados'
    )

    def __str__(self):
        return f"{self.titulo} ({self.condominio.nome})"

    class Meta:
        verbose_name = "Aviso"
        verbose_name_plural = "Avisos"
        ordering = ['-criado_em']
