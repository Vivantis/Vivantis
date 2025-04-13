from .models import Auditoria

# Função genérica para registrar ações no sistema
def registrar_acao(usuario, tipo_acao, entidade, objeto_id, descricao):
    """
    Salva um registro de auditoria com os dados informados.
    """
    Auditoria.objects.create(
        usuario=usuario,
        tipo_acao=tipo_acao,
        entidade=entidade,
        objeto_id=objeto_id,
        descricao=descricao
    )
