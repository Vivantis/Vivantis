# 🔔 Avisos
class Aviso(models.Model):
    titulo = models.CharField(max_length=150)
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    expira_em = models.DateTimeField(null=True, blank=True)
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE)
    publicado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.titulo} ({self.condominio.nome})"
