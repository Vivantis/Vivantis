import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from condominios.models import Unidade, Condominio

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
def setup_unidades(db):
    condominio = Condominio.objects.create(nome='Condomínio Alpha', endereco='Rua A')
    Unidade.objects.create(numero='101', bloco='A', condominio=condominio)
    Unidade.objects.create(numero='102', bloco='B', condominio=condominio)
    Unidade.objects.create(numero='201', bloco='A', condominio=condominio)
    return condominio

def test_listar_todas_unidades(cliente_autenticado, setup_unidades):
    response = cliente_autenticado.get('/api/unidades/')
    assert response.status_code == 200
    assert len(response.data["results"]) == 3  # Corrigido para acessar 'results'

def test_filtrar_por_numero(cliente_autenticado, setup_unidades):
    response = cliente_autenticado.get('/api/unidades/?numero=101')
    assert response.status_code == 200
    assert len(response.data["results"]) == 1
    assert response.data["results"][0]['numero'] == '101'

def test_filtrar_por_bloco(cliente_autenticado, setup_unidades):
    response = cliente_autenticado.get('/api/unidades/?bloco=A')
    assert response.status_code == 200
    assert len(response.data["results"]) == 2
    blocos = [u['bloco'] for u in response.data["results"]]
    assert all(b == 'A' for b in blocos)

def test_filtrar_por_condominio(cliente_autenticado, setup_unidades):
    condominio_id = setup_unidades.id
    response = cliente_autenticado.get(f'/api/unidades/?condominio={condominio_id}')
    assert response.status_code == 200
    assert len(response.data["results"]) == 3
