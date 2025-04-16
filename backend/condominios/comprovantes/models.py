# 📋 Comprovantes de Pagamento
class ComprovantePagamento(models.Model):
    cobranca = models.ForeignKey(Cobranca, on_delete=models.CASCADE)
    morador = models.ForeignKey(Morador, on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to='comprovantes/')
    comentario = models.TextField(blank=True)
    data_envio = models.DateTimeField(auto_now_add=True)
    validado = models.BooleanField(default=False)
    validado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='comprovantes_validados')

    def __str__(self):
        return f"Comprovante de {self.morador.nome} para {self.cobranca}"