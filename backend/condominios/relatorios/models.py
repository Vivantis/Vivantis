from django.db import models
from django.contrib.auth.models import User

# 📊 Relatório Gerado: registros de relatórios administrativos do sistema
class Relatorio(models.Model):
    titulo = models.CharField(max_length=100)
    tipo = models.CharField(
        max_length=50,
        help_text="Ex: Ocorrências, Reservas, Acessos, etc."
    )
    gerado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='relatorios_gerados')
    data_geracao = models.DateTimeField(auto_now_add=True)
    arquivo = models.FileField(upload_to='relatorios/', blank=True, null=True)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.tipo}"

    class Meta:
        verbose_name = "Relatório"
        verbose_name_plural = "Relatórios"
        ordering = ['-data_geracao']
