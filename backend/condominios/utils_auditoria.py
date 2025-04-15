import json
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
from .models import Auditoria

def registrar_acao(usuario, tipo_acao, instancia, descricao='', dados_anteriores=None):
    """
    Salva um registro de auditoria detalhado com:
    - usuário
    - tipo de ação (criado, editado, excluido)
    - nome do modelo
    - ID do objeto
    - descrição opcional
    - dados anteriores (opcional)
    - dados novos (extraído automaticamente da instância, se aplicável)
    """

    # Serializa dados anteriores, se existirem
    if dados_anteriores is not None:
        dados_anteriores = json.loads(json.dumps(dados_anteriores, cls=DjangoJSONEncoder))

    # Serializa os dados novos (do objeto atual)
    dados_novos = None
    if tipo_acao != 'excluido':
        dados_novos = json.loads(json.dumps(model_to_dict(instancia), cls=DjangoJSONEncoder))

    Auditoria.objects.create(
        usuario=usuario,
        tipo_acao=tipo_acao,
        entidade=instancia.__class__.__name__,
        objeto_id=str(instancia.pk),
        descricao=descricao,
        dados_anteriores=dados_anteriores,
        dados_novos=dados_novos
    )
