import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from condominios.condominio.models import Condominio
from condominios.espacoscomuns.models import EspacoComum


@pytest.fixture
def usuario_admin(db):
    return User.objects.create_user(username='admin', password='admin123')


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
def setup_condominio(db):
    # inclui todos os campos obrigatórios do modelo
    return Condominio.objects.create(
        nome='Condomínio Teste',
        endereco='Rua Central, 100',
        cidade='São Paulo',
        estado='SP',
        ativo=True
    )


def test_criar_espaco_comum(cliente_autenticado, setup_condominio):
    dados = {
        "nome": "Salão de Festas",
        "condominio": setup_condominio.id
    }
    response = cliente_autenticado.post('/api/espacos-comuns/', dados, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['nome'] == "Salão de Festas"


def test_listar_espacos_comuns(cliente_autenticado, setup_condominio):
    EspacoComum.objects.create(nome="Piscina", condominio=setup_condominio)
    response = cliente_autenticado.get('/api/espacos-comuns/')
    assert response.status_code == status.HTTP_200_OK

    # DRF padrão usa 'count' + 'results'
    assert response.data["count"] >= 1
    assert isinstance(response.data["results"], list)


def test_filtrar_espacos_por_nome(cliente_autenticado, setup_condominio):
    EspacoComum.objects.create(nome="Churrasqueira", condominio=setup_condominio)
    response = cliente_autenticado.get('/api/espacos-comuns/?search=Churras')
    assert response.status_code == status.HTTP_200_OK
    names = [e["nome"] for e in response.data["results"]]
    assert any("Churrasqueira" in n for n in names)


def test_atualizar_espaco_comum(cliente_autenticado, setup_condominio):
    espaco = EspacoComum.objects.create(nome="Salao Antigo", condominio=setup_condominio)
    novos_dados = {
        "nome": "Salão Novo",
        "condominio": setup_condominio.id
    }
    response = cliente_autenticado.put(f'/api/espacos-comuns/{espaco.id}/', novos_dados, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data["nome"] == "Salão Novo"


def test_deletar_espaco_comum(cliente_autenticado, setup_condominio):
    espaco = EspacoComum.objects.create(nome="Espaço Deletável", condominio=setup_condominio)
    response = cliente_autenticado.delete(f'/api/espacos-comuns/{espaco.id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not EspacoComum.objects.filter(id=espaco.id).exists()
