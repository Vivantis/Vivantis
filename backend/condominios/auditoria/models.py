from django.db import models
from django.contrib.auth.models import User

# 📄 Auditoria
class Auditoria(models.Model):
    """
    Registra ações realizadas no sistema, como criação, edição ou exclusão
    de objetos, mantendo o histórico de alterações.
    """

    ACOES = [
        ('criado', 'Criado'),
        ('editado', 'Editado'),
        ('excluido', 'Excluído'),
    ]

    usuario = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True,
        help_text="Usuário que realizou a ação"
    )
    tipo_acao = models.CharField(
        max_length=20, choices=ACOES,
        help_text="Tipo de ação registrada"
    )
    entidade = models.CharField(
        max_length=100,
        help_text="Nome da entidade afetada (ex: Morador, Unidade)"
    )
    objeto_id = models.CharField(
        max_length=100,
        help_text="ID do objeto afetado (pode ser int, UUID, etc.)"
    )
    descricao = models.TextField(
        blank=True,
        help_text="Descrição resumida da ação"
    )
    dados_anteriores = models.JSONField(null=True, blank=True)
    dados_novos = models.JSONField(null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data']
        verbose_name = "Registro de Auditoria"
        verbose_name_plural = "Registros de Auditoria"

    def __str__(self):
        return f"{self.entidade} #{self.objeto_id} - {self.get_tipo_acao_display()} ({self.data.strftime('%d/%m/%Y %H:%M')})"
