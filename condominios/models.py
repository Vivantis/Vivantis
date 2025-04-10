from django.db import models


# Modelo que representa um Condomínio
class Condominio(models.Model):
    nome = models.CharField(max_length=100)  # Nome do condomínio
    endereco = models.TextField()            # Endereço completo

    def __str__(self):
        return self.nome


# Modelo que representa uma Unidade dentro de um condomínio
class Unidade(models.Model):
    numero = models.CharField(max_length=10)                     
    bloco = models.CharField(max_length=10, null=True, blank=True)  # agora oficialmente opcional
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE)

    def __str__(self):
        return f"Apto {self.numero} - {self.condominio.nome}"



# Modelo que representa um Morador
class Morador(models.Model):
    nome = models.CharField(max_length=100)                      # Nome completo
    email = models.EmailField()                                  # E-mail do morador
    unidade = models.ForeignKey(
        Unidade,
        on_delete=models.CASCADE,
        null=True,   # Permite migração sem crash por registros antigos
        blank=True   # Permite deixar em branco em formulários/admin
    )

    def __str__(self):
        return self.nome


# Modelo que representa uma Ocorrência (chamado aberto pelo morador)
class Ocorrencia(models.Model):
    STATUS_CHOICES = [
        ('aberta', 'Aberta'),
        ('em_andamento', 'Em andamento'),
        ('resolvida', 'Resolvida'),
    ]

    titulo = models.CharField(max_length=100)                         # Título curto da ocorrência
    descricao = models.TextField()                                    # Descrição detalhada
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aberta')  # Status
    criado_em = models.DateTimeField(auto_now_add=True)               # Criada automaticamente
    atualizado_em = models.DateTimeField(auto_now=True)              # Atualizada automaticamente
    morador = models.ForeignKey(Morador, on_delete=models.CASCADE)   # Quem registrou
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)   # Unidade associada

    def __str__(self):
        return f"{self.titulo} - {self.get_status_display()}"

class Prestador(models.Model):
    # Nome do prestador
    nome = models.CharField(max_length=100)

    # Tipo de serviço (ex: limpeza, elétrica, jardinagem)
    tipo_servico = models.CharField(max_length=100)

    # Telefone de contato
    telefone = models.CharField(max_length=20)

    # Relacionamento com o condomínio onde presta serviço
    condominio = models.ForeignKey('Condominio', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome