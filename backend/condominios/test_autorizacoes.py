from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Condominio, Unidade, Morador, AutorizacaoEntrada

class AutorizacaoEntradaAPITests(APITestCase):
    """
    Testes para o módulo de autorização de entrada remota
    """

    def setUp(self):
        # Usuário da portaria (quem registra o pedido)
        self.user_portaria = User.objects.create_user(username='porteiro', password='123')
        self.client.force_authenticate(user=self.user_portaria)

        # Criação de condomínio e unidade
        self.condominio = Condominio.objects.create(nome="Condomínio Teste", endereco="Rua A, 123")
        self.unidade = Unidade.objects.create(numero="101", bloco="A", condominio=self.condominio)

        # Morador responsável pela unidade (quem autoriza)
        self.morador = Morador.objects.create(nome="João", email="joao@email.com", unidade=self.unidade)
        self.user_morador = User.objects.create_user(username='joao', email='joao@email.com', password='123')

        # Dados da solicitação
        self.dados = {
            "nome_visitante": "Carlos",
            "documento_visitante": "123456789",
            "unidade_destino": self.unidade.id,
            "observacoes": "Chegada prevista às 15h"
        }

    def test_criar_autorizacao(self):
        """Testa criação de uma solicitação de entrada"""
        response = self.client.post('/api/autorizacoes/', self.dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['status'], 'pendente')

    def test_listar_autorizacoes(self):
        """Testa listagem de autorizações"""
        AutorizacaoEntrada.objects.create(
            nome_visitante="Carlos",
            documento_visitante="123",
            unidade_destino=self.unidade,
            criado_por=self.user_portaria
        )
        response = self.client.get('/api/autorizacoes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_aprovar_autorizacao(self):
        """Testa aprovação de entrada por morador"""
        autorizacao = AutorizacaoEntrada.objects.create(
            nome_visitante="Carlos",
            documento_visitante="123",
            unidade_destino=self.unidade,
            criado_por=self.user_portaria
        )

        # Morador se autentica
        self.client.force_authenticate(user=self.user_morador)

        response = self.client.patch(f'/api/autorizacoes/{autorizacao.id}/', {
            "status": "aprovada"
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'aprovada')

    def test_recusar_autorizacao(self):
        """Testa recusa de entrada por morador"""
        autorizacao = AutorizacaoEntrada.objects.create(
            nome_visitante="Carlos",
            documento_visitante="123",
            unidade_destino=self.unidade,
            criado_por=self.user_portaria
        )

        self.client.force_authenticate(user=self.user_morador)

        response = self.client.patch(f'/api/autorizacoes/{autorizacao.id}/', {
            "status": "recusada"
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'recusada')
