from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from condominios.models import Visitante, Condominio, Unidade, Morador


class VisitanteAPITests(APITestCase):
    """
    Testes automatizados para a API de Visitantes
    """

    def setUp(self):
        # Criação do usuário autenticado
        self.user = User.objects.create_user(username='admin', password='admin123')
        self.client.force_authenticate(user=self.user)

        # Criação de dados relacionados
        self.condominio = Condominio.objects.create(nome="Condomínio Modelo", endereco="Rua XPTO, 1000")
        self.unidade = Unidade.objects.create(numero="A101", bloco="A", condominio=self.condominio)
        self.morador = Morador.objects.create(nome="Maria Moradora", email="maria@example.com", unidade=self.unidade)

        # Dados padrão para criação via API
        self.dados = {
            "nome": "Carlos Visitante",
            "documento": "123456789",
            "unidade": self.unidade.id,
            "morador_responsavel": self.morador.id
        }

    def test_criar_visitante(self):
        """Testa a criação de um novo visitante"""
        response = self.client.post('/api/visitantes/', self.dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nome'], self.dados['nome'])

    def test_listar_visitantes(self):
        """Testa a listagem de visitantes"""
        Visitante.objects.create(
            nome="Ana Visitante",
            documento="987654321",
            unidade=self.unidade,
            morador_responsavel=self.morador
        )
        response = self.client.get('/api/visitantes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data['results']), 1)

    def test_atualizar_visitante(self):
        """Testa a atualização dos dados de um visitante"""
        visitante = Visitante.objects.create(
            nome="João Antigo",
            documento="000111222",
            unidade=self.unidade,
            morador_responsavel=self.morador
        )
        novos_dados = {
            "nome": "João Atualizado",
            "documento": "000111222",
            "unidade": self.unidade.id,
            "morador_responsavel": self.morador.id
        }
        response = self.client.put(f'/api/visitantes/{visitante.id}/', novos_dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], "João Atualizado")

    def test_deletar_visitante(self):
        """Testa a exclusão de um visitante"""
        visitante = Visitante.objects.create(
            nome="Visitante Temporário",
            documento="999888777",
            unidade=self.unidade,
            morador_responsavel=self.morador
        )
        response = self.client.delete(f'/api/visitantes/{visitante.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Visitante.objects.filter(id=visitante.id).exists())

    def test_filtrar_visitantes(self):
        """Testa a filtragem de visitantes por nome, documento, unidade e morador_responsavel"""
        visitante1 = Visitante.objects.create(
            nome="Carlos Visitante",
            documento="123456789",
            unidade=self.unidade,
            morador_responsavel=self.morador
        )
        visitante2 = Visitante.objects.create(
            nome="Ana Visitante",
            documento="987654321",
            unidade=self.unidade,
            morador_responsavel=self.morador
        )

        # Filtrar por nome
        response = self.client.get(f'/api/visitantes/?nome=Carlos Visitante')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Carlos" in v["nome"] for v in response.data['results']))

        # Filtrar por documento
        response = self.client.get(f'/api/visitantes/?documento=987654321')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['documento'], "987654321")

        # Filtrar por unidade
        response = self.client.get(f'/api/visitantes/?unidade={self.unidade.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(v["unidade"] == self.unidade.id for v in response.data['results']))

        # Filtrar por morador responsável
        response = self.client.get(f'/api/visitantes/?morador_responsavel={self.morador.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(v["morador_responsavel"] == self.morador.id for v in response.data['results']))
