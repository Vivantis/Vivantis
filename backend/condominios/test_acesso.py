from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Condominio, Unidade, Morador, Prestador, Visitante, ControleAcesso


class ControleAcessoAPITests(APITestCase):
    """
    Testes automatizados para o módulo de Controle de Acesso
    """

    def setUp(self):
        # Criação e autenticação de usuário
        self.user = User.objects.create_user(username='admin', password='admin123')
        self.client.force_authenticate(user=self.user)

        # Dados base
        self.condominio = Condominio.objects.create(nome="Condomínio Central", endereco="Rua Principal, 123")
        self.unidade = Unidade.objects.create(numero="201", bloco="B", condominio=self.condominio)

        self.morador = Morador.objects.create(nome="João da Silva", email="joao@example.com", unidade=self.unidade)
        self.prestador = Prestador.objects.create(nome="Carlos Eletricista", tipo_servico="Elétrica", telefone="11999999999", condominio=self.condominio)
        self.visitante = Visitante.objects.create(nome="Ana Visitante", documento="123456789", unidade=self.unidade, morador_responsavel=self.morador)

        # Dados padrão para criação via API
        self.dados_morador = {
            "tipo": "morador",
            "morador": self.morador.id,
            "unidade": self.unidade.id,
            "observacoes": "Entrada autorizada"
        }

    def test_criar_acesso_morador(self):
        """Testa a criação de registro de acesso para morador"""
        response = self.client.post('/api/acessos/', self.dados_morador, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['tipo'], "morador")

    def test_listar_acessos(self):
        """Testa a listagem de acessos"""
        ControleAcesso.objects.create(
            tipo="visitante",
            visitante=self.visitante,
            unidade=self.unidade,
            observacoes="Visitante da manhã"
        )
        response = self.client.get('/api/acessos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_atualizar_acesso(self):
        """Testa a atualização do campo data_saida"""
        acesso = ControleAcesso.objects.create(
            tipo="prestador",
            prestador=self.prestador,
            unidade=self.unidade,
            observacoes="Entrada para manutenção"
        )
        novos_dados = {
            "tipo": "prestador",
            "prestador": self.prestador.id,
            "unidade": self.unidade.id,
            "data_saida": "2025-04-10T18:00:00Z",
            "observacoes": "Saiu às 18h"
        }
        response = self.client.put(f'/api/acessos/{acesso.id}/', novos_dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("data_saida", response.data)

    def test_deletar_acesso(self):
        """Testa a exclusão de um registro de acesso"""
        acesso = ControleAcesso.objects.create(
            tipo="morador",
            morador=self.morador,
            unidade=self.unidade,
            observacoes="Teste de exclusão"
        )
        response = self.client.delete(f'/api/acessos/{acesso.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(ControleAcesso.objects.filter(id=acesso.id).exists())
