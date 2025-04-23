from django.db import models

# 🚪 Controle de Acesso
class ControleAcesso(models.Model):
    """
    Registra entradas e saídas no condomínio por moradores, visitantes ou prestadores.
    """
    TIPO_CHOICES = [
        ('morador', 'Morador'),
        ('visitante', 'Visitante'),
        ('prestador', 'Prestador'),
    ]

    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    # Relacionamentos com outros módulos
    morador = models.ForeignKey('morador.Morador', on_delete=models.SET_NULL, null=True, blank=True)
    visitante = models.ForeignKey('visitante.Visitante', on_delete=models.SET_NULL, null=True, blank=True)
    prestador = models.ForeignKey('prestadores.Prestador', on_delete=models.SET_NULL, null=True, blank=True)
    unidade = models.ForeignKey('unidade.Unidade', on_delete=models.SET_NULL, null=True, blank=True)

    data_entrada = models.DateTimeField(auto_now_add=True)
    data_saida = models.DateTimeField(null=True, blank=True)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.get_tipo_display()} - Entrada: {self.data_entrada.strftime('%d/%m/%Y %H:%M')}"
