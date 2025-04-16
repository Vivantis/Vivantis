import json
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
from condominios.models import Auditoria


def registrar_acao(usuario, tipo_acao, instancia, descricao='', dados_anteriores=None):
    """
    Registra uma ação no histórico de auditoria.

    Parâmetros:
    - usuario: usuário responsável pela ação
    - tipo_acao: 'criado', 'editado' ou 'excluido'
    - instancia: instância do modelo afetado
    - descricao: texto descritivo opcional da ação
    - dados_anteriores: dicionário com os dados antigos (opcional)
    """

    # Serializa dados anteriores, se existirem
    if dados_anteriores is not None:
        dados_anteriores = json.loads(json.dumps(dados_anteriores, cls=DjangoJSONEncoder))

    # Serializa os dados novos (do objeto atual), exceto se for exclusão
    dados_novos = None
    if tipo_acao != 'excluido':
        dados_novos = json.loads(json.dumps(model_to_dict(instancia), cls=DjangoJSONEncoder))

    # Cria o registro de auditoria
    Auditoria.objects.create(
        usuario=usuario,
        tipo_acao=tipo_acao,
        entidade=instancia.__class__.__name__,
        objeto_id=str(instancia.pk),
        descricao=descricao or f"Ação {tipo_acao} registrada em {instancia.__class__.__name__}",
        dados_anteriores=dados_anteriores,
        dados_novos=dados_novos
    )
