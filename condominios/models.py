from django.db import models

# Modelo que representa um condomínio
class Condominio(models.Model):
    nome = models.CharField(max_length=100)  # Nome do condomínio
    endereco = models.TextField()            # Endereço completo

    def __str__(self):
        return self.nome

# Modelo que representa uma unidade/apartamento dentro de um condomínio
class Unidade(models.Model):
    numero = models.CharField(max_length=10)                             # Número da unidade
    bloco = models.CharField(max_length=50, blank=True, null=True)      # Bloco (opcional)
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE)  # Relacionamento com Condomínio

    def __str__(self):
        bloco_info = f" - Bloco {self.bloco}" if self.bloco else ""
        return f"Unidade {self.numero}{bloco_info} ({self.condominio.nome})"

# Modelo que representa um morador de uma unidade
class Morador(models.Model):
    nome = models.CharField(max_length=100)                              # Nome completo
    email = models.EmailField()                                          # Email de contato
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, null=True, blank=True)
    # Relacionamento com Unidade (temporariamente permite nulo para migração funcionar)

    def __str__(self):
        return self.nome
