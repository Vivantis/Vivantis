# 🚪 Controle de Acesso
from django.db import models
from .moradores.models import Morador
from .visitantes.models import Visitante
from .prestadores.models import Prestador
from .condominio.models import Unidade


class ControleAcesso(models.Model):
    TIPO_CHOICES = [
        ('morador', 'Morador'),
        ('visitante', 'Visitante'),
        ('prestador', 'Prestador'),
    ]

    # Define o tipo de pessoa que entrou no condomínio
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    # Relacionamentos opcionais, conforme o tipo selecionado
    morador = models.ForeignKey(Morador, on_delete=models.SET_NULL, null=True, blank=True)
    visitante = models.ForeignKey(Visitante, on_delete=models.SET_NULL, null=True, blank=True)
    prestador = models.ForeignKey(Prestador, on_delete=models.SET_NULL, null=True, blank=True)

    # Unidade vinculada à entrada (caso aplicável)
    unidade = models.ForeignKey(Unidade, on_delete=models.SET_NULL, null=True, blank=True)

    # Registro de datas de entrada e saída
    data_entrada = models.DateTimeField(auto_now_add=True)
    data_saida = models.DateTimeField(null=True, blank=True)

    # Campo livre para observações
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.get_tipo_display()} - Entrada: {self.data_entrada.strftime('%d/%m/%Y %H:%M')}"
