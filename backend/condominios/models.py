from django.db import models
from django.contrib.auth.models import User







































# 👨‍💻 Perfil do Usuário
class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=20, blank=True)
    foto = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"
