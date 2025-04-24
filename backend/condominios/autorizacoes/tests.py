from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

from condominios.condominio.models import Condominio
from condominios.unidade.models import Unidade
from condominios.morador.models import Morador
from condominios.autorizacoes.models import AutorizacaoEntrada


class AutorizacaoEntradaAPITests(APITestCase):
    """
    Testes para o módulo de autorização de entrada remota
    """

    def setUp(self):
        self.user_portaria = User.objects.create_user(username='porteiro', password='123')
        self.client.force_authenticate(user=self.user_portaria)

        self.condominio = Condominio.objects.create(nome="Condomínio Teste", endereco="Rua A, 123")
        self.unidade = Unidade.objects.create(numero="101", bloco="A", condominio=self.condominio)
        self.morador = Morador.objects.create(
            nome="João", email="joao@email.com", unidade=self.unidade
        )
        self.user_morador = User.objects.create_user(
            username='joao', email=self.morador.email, password='123'
        )

        self.payload = {
            "nome_visitante": "Carlos",
            "documento_visitante": "123456789",
            "unidade_destino": self.unidade.id,
            "observacoes": "Chegada prevista às 15h"
        }

    def test_criar_autorizacao(self):
        response = self.client.post('/api/autorizacoes/', self.payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['status'], 'pendente')

    def test_listar_autorizacoes(self):
        AutorizacaoEntrada.objects.create(
            nome_visitante="Carlos",
            documento_visitante="123",
            unidade_destino=self.unidade,
            criado_por=self.user_portaria
        )
        response = self.client.get('/api/autorizacoes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # DRF paginated
        self.assertGreaterEqual(len(response.data['results']), 1)

    def test_aprovar_autorizacao(self):
        auth = AutorizacaoEntrada.objects.create(
            nome_visitante="Carlos",
            documento_visitante="123",
            unidade_destino=self.unidade,
            criado_por=self.user_portaria
        )
        # Morador aprova
        self.client.force_authenticate(user=self.user_morador)
        response = self.client.patch(
            f'/api/autorizacoes/{auth.id}/',
            {"status": "aprovada"},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'aprovada')

    def test_recusar_autorizacao(self):
        auth = AutorizacaoEntrada.objects.create(
            nome_visitante="Carlos",
            documento_visitante="123",
            unidade_destino=self.unidade,
            criado_por=self.user_portaria
        )
        self.client.force_authenticate(user=self.user_morador)
        response = self.client.patch(
            f'/api/autorizacoes/{auth.id}/',
            {"status": "recusada"},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'recusada')
