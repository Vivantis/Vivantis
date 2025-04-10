from django.db import models

# Modelo que representa um Condomínio
class Condominio(models.Model):
    nome = models.CharField(max_length=100)  # Nome do condomínio
    endereco = models.TextField()            # Endereço completo

    def __str__(self):
        return self.nome  # Representação legível no admin/painéis


# Modelo que representa uma Unidade dentro de um condomínio
class Unidade(models.Model):
    numero = models.CharField(max_length=10)                     # Número do apartamento, sala, etc.
    bloco = models.CharField(max_length=10, blank=True)          # Bloco (se aplicável)
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE)  # Relação com o condomínio

    def __str__(self):
        # Exibe: "Apto 101 - Condomínio Sol Nascente"
        return f"Apto {self.numero} - {self.condominio.nome}"


# Modelo que representa um Morador
class Morador(models.Model):
    nome = models.CharField(max_length=100)                      # Nome completo
    email = models.EmailField()                                  # E-mail do morador
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)  # Relação com a unidade

    def __str__(self):
        return self.nome
