from django.db import models
from django.contrib.auth.models import User

# 🏢 Modelo que representa um Condomínio
class Condominio(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.TextField()
    cidade = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=2, blank=True, null=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


# 🏠 Unidade
class Unidade(models.Model):
    numero = models.CharField(max_length=10)
    bloco = models.CharField(max_length=10, null=True, blank=True)
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE)

    def __str__(self):
        return f"Apto {self.numero} - {self.condominio.nome}"


# 👤 Morador
class Morador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='morador', null=True)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, blank=True, null=True)
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


# 🚰 Prestador
class Prestador(models.Model):
    nome = models.CharField(max_length=100)
    tipo_servico = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


# 📢 Ocorrência
class Ocorrencia(models.Model):
    STATUS_CHOICES = [
        ('aberta', 'Aberta'),
        ('em_andamento', 'Em andamento'),
        ('resolvida', 'Resolvida'),
    ]

    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aberta')
    data_registro = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    morador = models.ForeignKey(Morador, on_delete=models.CASCADE)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} - {self.get_status_display()}"


# 👥 Visitante
class Visitante(models.Model):
    nome = models.CharField(max_length=100)
    documento = models.CharField(max_length=50)
    data_visita = models.DateTimeField(auto_now_add=True)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    morador_responsavel = models.ForeignKey(Morador, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - Unidade {self.unidade}"


# 🚪 Controle de Acesso
class ControleAcesso(models.Model):
    TIPO_CHOICES = [
        ('morador', 'Morador'),
        ('visitante', 'Visitante'),
        ('prestador', 'Prestador'),
    ]

    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    morador = models.ForeignKey(Morador, on_delete=models.SET_NULL, null=True, blank=True)
    visitante = models.ForeignKey(Visitante, on_delete=models.SET_NULL, null=True, blank=True)
    prestador = models.ForeignKey(Prestador, on_delete=models.SET_NULL, null=True, blank=True)
    unidade = models.ForeignKey(Unidade, on_delete=models.SET_NULL, null=True, blank=True)
    data_entrada = models.DateTimeField(auto_now_add=True)
    data_saida = models.DateTimeField(null=True, blank=True)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.get_tipo_display()} - Entrada: {self.data_entrada.strftime('%d/%m/%Y %H:%M')}"


# 📦 Correspondência
class Correspondencia(models.Model):
    descricao = models.CharField(max_length=200)
    morador = models.ForeignKey(Morador, on_delete=models.CASCADE)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    data_recebimento = models.DateTimeField(auto_now_add=True)
    data_retirada = models.DateTimeField(null=True, blank=True)
    entregue_por = models.CharField(max_length=100, blank=True)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.descricao} - {self.morador.nome}"


# 🏛️ Espaços Comuns
class EspacoComum(models.Model):
    nome = models.CharField(max_length=100)
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} ({self.condominio.nome})"


# 🗓️ Reserva de Espaços
class ReservaEspaco(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovado', 'Aprovado'),
        ('cancelado', 'Cancelado'),
    ]

    morador = models.ForeignKey(Morador, on_delete=models.CASCADE)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    espaco = models.ForeignKey(EspacoComum, on_delete=models.CASCADE)
    data = models.DateField()
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.espaco.nome} - {self.data} ({self.get_status_display()})"


# 📂 Documentos
class Documento(models.Model):
    TIPO_CHOICES = [
        ('regulamento', 'Regulamento Interno'),
        ('ata', 'Ata de Reunião'),
        ('edital', 'Edital'),
        ('boleto', 'Boleto'),
        ('outro', 'Outro'),
    ]

    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='outro')
    arquivo = models.FileField(upload_to='documentos/')
    visivel_para_moradores = models.BooleanField(default=True)
    data_envio = models.DateTimeField(auto_now_add=True)
    enviado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} - {self.get_tipo_display()}"


# 👨‍💼 Administrador Geral
class AdministradorGeral(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


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


# 🔧 Manutenções
class Manutencao(models.Model):
    STATUS_CHOICES = [
        ('planejada', 'Planejada'),
        ('em_andamento', 'Em andamento'),
        ('concluida', 'Concluída'),
    ]

    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planejada')
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE)
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} - {self.get_status_display()}"


# 💸 Cobranças
class Cobranca(models.Model):
    TIPO_CHOICES = [
        ('mensalidade', 'Mensalidade'),
        ('fundo_reserva', 'Fundo de Reserva'),
        ('extraordinaria', 'Extraordinária'),
        ('outro', 'Outro'),
    ]
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('pago', 'Pago'),
        ('atrasado', 'Atrasado'),
    ]

    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    morador = models.ForeignKey(Morador, on_delete=models.SET_NULL, null=True, blank=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='mensalidade')
    descricao = models.CharField(max_length=200, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    vencimento = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.unidade} - R$ {self.valor} - {self.get_status_display()}"


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


# 🗒️ Autorização Remota
class AutorizacaoEntrada(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovada', 'Aprovada'),
        ('recusada', 'Recusada'),
    ]

    nome_visitante = models.CharField(max_length=100)
    documento_visitante = models.CharField(max_length=50)
    unidade_destino = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    criado_em = models.DateTimeField(auto_now_add=True)
    respondido_em = models.DateTimeField(null=True, blank=True)
    respondido_por = models.ForeignKey(Morador, on_delete=models.SET_NULL, null=True, blank=True)
    criado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nome_visitante} para {self.unidade_destino} - {self.get_status_display()}"


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
    descricao = models.TextField(blank=True)  # Você pode preencher manualmente se quiser explicar algo
    dados_anteriores = models.JSONField(null=True, blank=True)
    dados_novos = models.JSONField(null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.entidade} #{self.objeto_id} - {self.get_tipo_acao_display()}"



# 👨‍💻 Perfil do Usuário
class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=20, blank=True)
    foto = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"
