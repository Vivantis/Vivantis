from django.db import models


# ─────────────────────────────────────────────────────────────
# 🏢 Modelo que representa um Condomínio
# ─────────────────────────────────────────────────────────────
class Condominio(models.Model):
    nome = models.CharField(max_length=100)  # Nome do condomínio
    endereco = models.TextField()            # Endereço completo

    def __str__(self):
        return self.nome


# ─────────────────────────────────────────────────────────────
# 🏠 Modelo que representa uma Unidade dentro de um condomínio
# ─────────────────────────────────────────────────────────────
class Unidade(models.Model):
    numero = models.CharField(max_length=10)                     
    bloco = models.CharField(max_length=10, null=True, blank=True)  # Opcional
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE)

    def __str__(self):
        return f"Apto {self.numero} - {self.condominio.nome}"


# ─────────────────────────────────────────────────────────────
# 👤 Modelo que representa um Morador
# ─────────────────────────────────────────────────────────────
class Morador(models.Model):
    nome = models.CharField(max_length=100)                      # Nome completo
    email = models.EmailField()                                  # E-mail do morador
    unidade = models.ForeignKey(
        Unidade,
        on_delete=models.CASCADE,
        null=True,   # Permite registros antigos sem unidade
        blank=True   # Permite campo em branco em formulários
    )

    def __str__(self):
        return self.nome


# ─────────────────────────────────────────────────────────────
# 🛠️ Modelo que representa um Prestador de Serviços
# ─────────────────────────────────────────────────────────────
class Prestador(models.Model):
    nome = models.CharField(max_length=100)           # Nome do prestador
    tipo_servico = models.CharField(max_length=100)   # Tipo de serviço (ex: Limpeza)
    telefone = models.CharField(max_length=20)        # Telefone de contato
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE)  # Associação ao condomínio

    def __str__(self):
        return self.nome


# ─────────────────────────────────────────────────────────────
# 📢 Modelo que representa uma Ocorrência (aberta por morador)
# ─────────────────────────────────────────────────────────────
class Ocorrencia(models.Model):
    STATUS_CHOICES = [
        ('aberta', 'Aberta'),
        ('em_andamento', 'Em andamento'),
        ('resolvida', 'Resolvida'),
    ]

    titulo = models.CharField(max_length=100)                        # Título da ocorrência
    descricao = models.TextField()                                   # Detalhes
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aberta')  # Status atual
    criado_em = models.DateTimeField(auto_now_add=True)              # Timestamp de criação
    atualizado_em = models.DateTimeField(auto_now=True)              # Timestamp de última edição
    morador = models.ForeignKey(Morador, on_delete=models.CASCADE)   # Quem abriu
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)   # Unidade associada

    def __str__(self):
        return f"{self.titulo} - {self.get_status_display()}"


# ─────────────────────────────────────────────────────────────
# 👥 Modelo que representa um Visitante
# ─────────────────────────────────────────────────────────────
class Visitante(models.Model):
    nome = models.CharField(max_length=100)             # Nome completo do visitante
    documento = models.CharField(max_length=50)         # Documento de identificação (RG, CPF, etc.)
    data_visita = models.DateTimeField(auto_now_add=True)  # Data e hora da visita
    
    unidade = models.ForeignKey(
        Unidade,
        on_delete=models.CASCADE,
        help_text="Unidade que está recebendo o visitante"
    )

    morador_responsavel = models.ForeignKey(
        Morador,
        on_delete=models.CASCADE,
        help_text="Morador que autorizou a entrada"
    )

    def __str__(self):
        return f"{self.nome} - Unidade {self.unidade}"

# ─────────────────────────────────────────────────────────────
# 🚪 Modelo de Controle de Acesso
# ─────────────────────────────────────────────────────────────
class ControleAcesso(models.Model):
    TIPO_CHOICES = [
        ('morador', 'Morador'),
        ('visitante', 'Visitante'),
        ('prestador', 'Prestador'),
    ]

    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)  # Define o tipo de pessoa
    morador = models.ForeignKey('Morador', on_delete=models.SET_NULL, null=True, blank=True)
    visitante = models.ForeignKey('Visitante', on_delete=models.SET_NULL, null=True, blank=True)
    prestador = models.ForeignKey('Prestador', on_delete=models.SET_NULL, null=True, blank=True)

    data_entrada = models.DateTimeField(auto_now_add=True)  # Registrado automaticamente ao entrar
    data_saida = models.DateTimeField(null=True, blank=True)  # Pode ser registrado depois

    unidade = models.ForeignKey('Unidade', on_delete=models.SET_NULL, null=True, blank=True)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.get_tipo_display()} - Entrada: {self.data_entrada.strftime('%d/%m/%Y %H:%M')}"

# ─────────────────────────────────────────────────────────────
# 📦 Modelo de Correspondência (entregas e encomendas)
# ─────────────────────────────────────────────────────────────
class Correspondencia(models.Model):
    descricao = models.CharField(max_length=200)  # Ex: "Encomenda da Amazon", "Carta registrada"
    morador = models.ForeignKey('Morador', on_delete=models.CASCADE)  # Destinatário
    unidade = models.ForeignKey('Unidade', on_delete=models.CASCADE)  # Unidade relacionada

    data_recebimento = models.DateTimeField(auto_now_add=True)  # Quando foi recebida na portaria
    data_retirada = models.DateTimeField(null=True, blank=True)  # Quando foi retirada (se já foi)

    entregue_por = models.CharField(max_length=100, blank=True)  # Ex: Correios, Mercado Livre
    observacoes = models.TextField(blank=True)  # Qualquer anotação adicional

    def __str__(self):
        return f"{self.descricao} - {self.morador.nome}"

# ─────────────────────────────────────────────────────────────
# 🧱 Modelo de Espaços Comuns (ex: salão, churrasqueira)
# ─────────────────────────────────────────────────────────────
class EspacoComum(models.Model):
    nome = models.CharField(max_length=100)  # Ex: "Salão de Festas", "Churrasqueira"
    condominio = models.ForeignKey('Condominio', on_delete=models.CASCADE)  # Qual condomínio possui esse espaço

    def __str__(self):
        return f"{self.nome} ({self.condominio.nome})"




# ─────────────────────────────────────────────────────────────
# 📅 Modelo de Reserva de Espaço
# ─────────────────────────────────────────────────────────────
class ReservaEspaco(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovado', 'Aprovado'),
        ('cancelado', 'Cancelado'),
    ]

    morador = models.ForeignKey('Morador', on_delete=models.CASCADE)
    unidade = models.ForeignKey('Unidade', on_delete=models.CASCADE)
    espaco = models.ForeignKey('EspacoComum', on_delete=models.CASCADE)

    data_reserva = models.DateField()
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.espaco.nome} - {self.data_reserva} ({self.get_status_display()})"

from django.contrib.auth.models import User

# ─────────────────────────────────────────────────────────────
# 📂 Modelo de Documentos do Condomínio
# ─────────────────────────────────────────────────────────────
class Documento(models.Model):
    TIPO_CHOICES = [
        ('regulamento', 'Regulamento Interno'),
        ('ata', 'Ata de Reunião'),
        ('edital', 'Edital'),
        ('boleto', 'Boleto'),
        ('outro', 'Outro'),
    ]

    titulo = models.CharField(max_length=200)  # Nome ou assunto do documento
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='outro')
    arquivo = models.FileField(upload_to='documentos/')  # Upload do arquivo
    visivel_para_moradores = models.BooleanField(default=True)  # Exibir ou não
    data_envio = models.DateTimeField(auto_now_add=True)  # Registro de envio

    enviado_por = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True,
        help_text="Usuário que fez o upload"
    )

    condominio = models.ForeignKey(
        Condominio,
        on_delete=models.CASCADE,
        help_text="Condomínio ao qual o documento pertence"
    )

    def __str__(self):
        return f"{self.titulo} - {self.get_tipo_display()}"

# ─────────────────────────────────────────────────────────────
# 👨‍💼 Modelo de Administrador Geral (gestor externo)
# ─────────────────────────────────────────────────────────────
class AdministradorGeral(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

# ─────────────────────────────────────────────────────────────
# 🔔 Modelo de Avisos e Comunicados
# ─────────────────────────────────────────────────────────────
class Aviso(models.Model):
    titulo = models.CharField(max_length=150)  # Ex: "Reunião de condomínio"
    mensagem = models.TextField()              # Conteúdo completo do aviso
    criado_em = models.DateTimeField(auto_now_add=True)
    expira_em = models.DateTimeField(null=True, blank=True)

    condominio = models.ForeignKey(
        Condominio,
        on_delete=models.CASCADE,
        help_text="Condomínio onde o aviso será exibido"
    )

    publicado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        help_text="Usuário que publicou o aviso"
    )

    def __str__(self):
        return f"{self.titulo} ({self.condominio.nome})"

# ─────────────────────────────────────────────────────────────
# 🔧 Modelo de Manutenção
# ─────────────────────────────────────────────────────────────
class Manutencao(models.Model):
    STATUS_CHOICES = [
        ('planejada', 'Planejada'),
        ('em_andamento', 'Em andamento'),
        ('concluida', 'Concluída'),
    ]

    titulo = models.CharField(max_length=150)  # Título da manutenção (ex: "Manutenção do elevador")
    descricao = models.TextField()              # Descrição detalhada
    data_inicio = models.DateTimeField()       # Data de início da manutenção
    data_fim = models.DateTimeField()          # Data de fim da manutenção
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planejada')
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE)
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE)  # Quem registrou a manutenção

    def __str__(self):
        return f"{self.titulo} - {self.get_status_display()}"

# ─────────────────────────────────────────────────────────────
# 💸 Modelo de Cobrança Financeira (ex: taxa condominial)
# ─────────────────────────────────────────────────────────────
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

    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)  # Unidade que está sendo cobrada
    morador = models.ForeignKey(Morador, on_delete=models.SET_NULL, null=True, blank=True)  # Opcional
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='mensalidade')
    descricao = models.CharField(max_length=200, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    vencimento = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.unidade} - R$ {self.valor} - {self.get_status_display()}"


# ─────────────────────────────────────────────────────────────
# 📎 Modelo de Comprovante de Pagamento
# ─────────────────────────────────────────────────────────────
class ComprovantePagamento(models.Model):
    cobranca = models.ForeignKey('Cobranca', on_delete=models.CASCADE)  # Referência à cobrança
    morador = models.ForeignKey('Morador', on_delete=models.CASCADE)    # Morador que enviou o comprovante
    arquivo = models.FileField(upload_to='comprovantes/')               # Arquivo enviado (imagem/PDF)
    comentario = models.TextField(blank=True)                           # Comentário opcional
    data_envio = models.DateTimeField(auto_now_add=True)                # Registrado automaticamente

    validado = models.BooleanField(default=False)                       # Marcado como validado ou não
    validado_por = models.ForeignKey(                                   
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='comprovantes_validados',
        help_text="Usuário que validou o comprovante"
    )

    def __str__(self):
        return f"Comprovante de {self.morador.nome} para {self.cobranca}"

# ─────────────────────────────────────────────────────────────
# ✅ Modelo de Autorização de Entrada Remota
# ─────────────────────────────────────────────────────────────
class AutorizacaoEntrada(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovada', 'Aprovada'),
        ('recusada', 'Recusada'),
    ]

    nome_visitante = models.CharField(max_length=100)  # Nome do visitante
    documento_visitante = models.CharField(max_length=50)  # RG, CPF, etc.

    unidade_destino = models.ForeignKey(
        Unidade,
        on_delete=models.CASCADE,
        help_text="Unidade que o visitante quer acessar"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pendente',
        help_text="Status da autorização"
    )

    criado_em = models.DateTimeField(auto_now_add=True)  # Quando a solicitação foi registrada
    respondido_em = models.DateTimeField(null=True, blank=True)  # Quando foi respondida

    respondido_por = models.ForeignKey(
        Morador,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Morador que autorizou ou recusou"
    )

    criado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Usuário da portaria que registrou a solicitação"
    )

    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nome_visitante} para {self.unidade_destino} - {self.get_status_display()}"
