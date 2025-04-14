from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from condominios.models import Condominio, Unidade, Morador, Prestador, Visitante, ControleAcesso


class ControleAcessoAPITests(APITestCase):
    """
    Testes automatizados para o módulo de Controle de Acesso com filtros
    """

    def setUp(self):
        # Criação e autenticação de usuário
        self.user = User.objects.create_user(username='admin', password='admin123')
        self.client.force_authenticate(user=self.user)

        # Dados base
        self.condominio = Condominio.objects.create(nome="Condomínio Central", endereco="Rua Principal, 123")
        self.unidade = Unidade.objects.create(numero="201", bloco="B", condominio=self.condominio)
        self.unidade2 = Unidade.objects.create(numero="301", bloco="B", condominio=self.condominio)

        self.morador = Morador.objects.create(nome="João da Silva", email="joao@example.com", unidade=self.unidade)
        self.prestador = Prestador.objects.create(nome="Carlos Eletricista", tipo_servico="Elétrica", telefone="11999999999", condominio=self.condominio)
        self.visitante = Visitante.objects.create(nome="Ana Visitante", documento="123456789", unidade=self.unidade, morador_responsavel=self.morador)

        # Registros de acesso
        self.acesso_morador = ControleAcesso.objects.create(
            tipo="morador",
            morador=self.morador,
            unidade=self.unidade,
            observacoes="Entrada morador"
        )

        self.acesso_visitante = ControleAcesso.objects.create(
            tipo="visitante",
            visitante=self.visitante,
            unidade=self.unidade,
            observacoes="Entrada visitante"
        )

        self.acesso_prestador = ControleAcesso.objects.create(
            tipo="prestador",
            prestador=self.prestador,
            unidade=self.unidade2,
            observacoes="Entrada prestador"
        )

    def test_criar_acesso_morador(self):
        """Testa a criação de registro de acesso para morador"""
        dados = {
            "tipo": "morador",
            "morador": self.morador.id,
            "unidade": self.unidade.id,
            "observacoes": "Entrada autorizada"
        }
        response = self.client.post('/api/acessos/', dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['tipo'], "morador")

    def test_listar_acessos(self):
        """Testa a listagem de todos os acessos"""
        response = self.client.get('/api/acessos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data['results']), 3)

    def test_filtrar_por_tipo(self):
        """Testa filtragem por tipo de acesso"""
        response = self.client.get('/api/acessos/?tipo=visitante')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(a['tipo'] == 'visitante' for a in response.data['results']))

    def test_filtrar_por_morador(self):
        """Testa filtragem por morador"""
        response = self.client.get(f'/api/acessos/?morador={self.morador.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(a['morador'] == self.morador.id for a in response.data['results']))

    def test_filtrar_por_visitante(self):
        """Testa filtragem por visitante"""
        response = self.client.get(f'/api/acessos/?visitante={self.visitante.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(a['visitante'] == self.visitante.id for a in response.data['results']))

    def test_filtrar_por_prestador(self):
        """Testa filtragem por prestador"""
        response = self.client.get(f'/api/acessos/?prestador={self.prestador.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(a['prestador'] == self.prestador.id for a in response.data['results']))

    def test_filtrar_por_unidade(self):
        """Testa filtragem por unidade"""
        response = self.client.get(f'/api/acessos/?unidade={self.unidade.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(a['unidade'] == self.unidade.id for a in response.data['results']))

    def test_atualizar_acesso(self):
        """Testa a atualização do campo data_saida"""
        dados = {
            "tipo": "morador",
            "morador": self.morador.id,
            "unidade": self.unidade.id,
            "data_saida": "2025-04-15T18:00:00Z",
            "observacoes": "Saiu às 18h"
        }
        response = self.client.put(f'/api/acessos/{self.acesso_morador.id}/', dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("data_saida", response.data)

    def test_deletar_acesso(self):
        """Testa a exclusão de um registro de acesso"""
        acesso = ControleAcesso.objects.create(
            tipo="morador",
            morador=self.morador,
            unidade=self.unidade,
            observacoes="Acesso temporário"
        )
        response = self.client.delete(f'/api/acessos/{acesso.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(ControleAcesso.objects.filter(id=acesso.id).exists())
