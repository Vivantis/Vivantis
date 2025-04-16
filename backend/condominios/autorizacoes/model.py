# 🗒️ AutorizacaoEntrada model
from django.db import models
from django.contrib.auth.models import User
from condominios.models import Unidade, Morador

class AutorizacaoEntrada(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovada', 'Aprovada'),
        ('recusada', 'Recusada'),
    ]

    nome_visitante = models.CharField(max_length=100)
    documento_visitante = models.CharField(max_length=50)
    unidade_destino = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente', db_index=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    respondido_em = models.DateTimeField(null=True, blank=True)
    respondido_por = models.ForeignKey(
        Morador,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='autorizacoes_respondidas'
    )
    criado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='autorizacoes_criadas'
    )
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nome_visitante} para {self.unidade_destino} - {self.get_status_display()}"
