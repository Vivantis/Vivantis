# 👤 Morador
class Morador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='morador', null=True)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, blank=True, null=True)  # <--- corrigido aqui
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    foto = models.ImageField(upload_to='fotos_moradores/', null=True, blank=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    rg = models.CharField(max_length=20, blank=True, null=True)
    is_proprietario = models.BooleanField(default=False)
    is_inquilino = models.BooleanField(default=False)
    pode_votar = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
