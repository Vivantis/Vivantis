from django.db import models
from condominios.unidade.models import Unidade
from condominios.morador.models import Morador

# 💸 Cobranças vinculadas às unidades/moradores
class Cobranca(models.Model):
    TIPO_CHOICES = [
        ('mensalidade', 'Mensalidade'),
        ('fundo_reserva', 'Fundo de Reserva'),
        ('extraordinaria', 'Extraordinária'),
        ('outro', 'Outro'),
    ]

    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('pago', 'Pago'),
        ('atrasado', 'Atrasado'),
    ]

    unidade = models.ForeignKey(
        Unidade,
        on_delete=models.CASCADE,
        related_name='cobrancas'
    )

    morador = models.ForeignKey(
        Morador,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='cobrancas'
    )

    tipo = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES,
        default='mensalidade'
    )

    descricao = models.CharField(max_length=200, blank=True)

    valor = models.DecimalField(max_digits=10, decimal_places=2)
    vencimento = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pendente',
        db_index=True
    )

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.unidade} - R$ {self.valor:.2f} - {self.get_status_display()}"

    class Meta:
        verbose_name = "Cobrança"
        verbose_name_plural = "Cobranças"
        ordering = ['-vencimento']
