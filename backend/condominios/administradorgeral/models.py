from django.db import models
from django.contrib.auth.models import User

# 👨‍💼 Administrador Geral
class AdministradorGeral(models.Model):
    """
    Representa um administrador geral do sistema, vinculado a um usuário Django.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.user.username})"
