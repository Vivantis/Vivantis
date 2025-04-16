from django.db import models
from django.contrib.auth.models import User

# 📄 Auditoria
class Auditoria(models.Model):
    ACOES = [
        ('criado', 'Criado'),
        ('editado', 'Editado'),
        ('excluido', 'Excluído'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    tipo_acao = models.CharField(max_length=20, choices=ACOES)
    entidade = models.CharField(max_length=100)  # Nome do modelo (ex: Morador)
    objeto_id = models.CharField(max_length=100)  # Pode ser UUID, inteiro ou string
    descricao = models.TextField(blank=True)
    dados_anteriores = models.JSONField(null=True, blank=True)
    dados_novos = models.JSONField(null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.entidade} #{self.objeto_id} - {self.get_tipo_acao_display()}"

    class Meta:
        ordering = ['-data']  # Auditorias mais recentes primeiro
