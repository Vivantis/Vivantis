from django.db import models
from condominios.condominio.models import Condominio

# 💼 Prestador de Serviço: cadastro de profissionais e empresas que atuam no condomínio
class Prestador(models.Model):
    nome = models.CharField(max_length=100)
    tipo_servico = models.CharField(max_length=100)
    documento = models.CharField(max_length=30, blank=True, null=True)  # CPF ou CNPJ
    telefone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True, null=True)
    ativo = models.BooleanField(default=True)
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='prestadores')

    def __str__(self):
        return f"{self.nome} ({self.tipo_servico})"

    class Meta:
        verbose_name = "Prestador de Serviço"
        verbose_name_plural = "Prestadores de Serviço"
        ordering = ['nome']
