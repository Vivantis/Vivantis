from django.db import models
from condominios.morador.models import Morador
from condominios.unidade.models import Unidade
from condominios.espacoscomuns.models import EspacoComum



# 🗓️ Reserva de Espaços Comuns pelos moradores
class ReservaEspaco(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovado', 'Aprovado'),
        ('cancelado', 'Cancelado'),
    ]

    morador = models.ForeignKey(Morador, on_delete=models.CASCADE, related_name='reservas')
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, related_name='reservas')
    espaco = models.ForeignKey(EspacoComum, on_delete=models.CASCADE, related_name='reservas')
    data = models.DateField()
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    observacoes = models.TextField(blank=True)

    class Meta:
        verbose_name = "Reserva de Espaço"
        verbose_name_plural = "Reservas de Espaços"
        ordering = ['-data']
        constraints = [
            models.UniqueConstraint(
                fields=['espaco', 'data', 'horario_inicio', 'horario_fim'],
                name='unique_reserva_por_horario'
            )
        ]

    def __str__(self):
        return f"{self.espaco.nome} - {self.data} ({self.get_status_display()})"
