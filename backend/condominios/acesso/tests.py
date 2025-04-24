import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

from condominios.condominio.models import Condominio
from condominios.unidade.models import Unidade
from condominios.morador.models import Morador
from condominios.visitante.models import Visitante
from condominios.prestadores.models import Prestador
from condominios.acesso.models import ControleAcesso


@pytest.fixture
def usuario_admin(db):
    user = User.objects.create_user(username='admin', password='admin123')
    return user


@pytest.fixture
def token_autenticacao(usuario_admin):
    refresh = RefreshToken.for_user(usuario_admin)
    return str(refresh.access_token)


@pytest.fixture
def cliente_autenticado(token_autenticacao):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + token_autenticacao)
    return client


@pytest.fixture
def setup_acesso(db):
    condominio = Condominio.objects.create(
        nome="Residencial Teste", endereco="Rua Exemplo"
    )
    unidade = Unidade.objects.create(
        numero="101", bloco="A", condominio=condominio
    )
    morador = Morador.objects.create(
        nome="João", email="joao@email.com", unidade=unidade
    )
    Visitante.objects.create(
        nome="Carlos", documento="123456789", unidade=unidade
    )
    prestador = Prestador.objects.create(
        nome="Limpeza LTDA", servico="Limpeza", condominio=condominio
    )
    return {"unidade": unidade, "morador": morador, "prestador": prestador}


def test_criar_acesso_morador(cliente_autenticado, setup_acesso):
    morador = setup_acesso["morador"]
    unidade = setup_acesso["unidade"]
    dados = {
        "tipo": "morador",
        "morador": morador.id,
        "unidade": unidade.id,
        "observacoes": "Entrada pelo portão principal"
    }
    response = cliente_autenticado.post("/api/acessos/", dados, format="json")
    assert response.status_code == 201
    assert response.data["tipo"] == "morador"


def test_listar_acessos(cliente_autenticado):
    response = cliente_autenticado.get("/api/acessos/")
    assert response.status_code == 200


def test_filtrar_por_tipo(cliente_autenticado, setup_acesso):
    morador = setup_acesso["morador"]
    unidade = setup_acesso["unidade"]
    ControleAcesso.objects.create(tipo="morador", morador=morador, unidade=unidade)
    response = cliente_autenticado.get("/api/acessos/?tipo=morador")
    assert response.status_code == 200
    for acesso in response.data.get("results", []):
        assert acesso["tipo"] == "morador"
