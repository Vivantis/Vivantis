from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from condominios.condominio.models import Condominio
from condominios.unidade.models import Unidade
from condominios.morador.models import Morador
from condominios.correspondencia.models import Correspondencia


class CorrespondenciaAPITests(APITestCase):
    """
    Testes automatizados para a API de Correspondências, incluindo criação, leitura, atualização,
    exclusão e filtros por morador, unidade e entregador.
    """

    def setUp(self):
        # Cria e autentica um usuário
        self.user = User.objects.create_user(username='admin', password='admin123')
        self.client.force_authenticate(user=self.user)

        # Cria dados relacionados
        self.condominio = Condominio.objects.create(nome="Condomínio Nova Era", endereco="Av. Central, 456")
        self.unidade = Unidade.objects.create(numero="302", bloco="C", condominio=self.condominio)
        self.morador = Morador.objects.create(nome="Carlos Morador", email="carlos@example.com", unidade=self.unidade)

        # Correspondência padrão
        self.correspondencia = Correspondencia.objects.create(
            descricao="Encomenda da Amazon",
            morador=self.morador,
            unidade=self.unidade,
            entregue_por="Correios",
            observacoes="Caixa pequena"
        )

    def test_criar_correspondencia(self):
        """Testa a criação de uma nova correspondência"""
        dados = {
            "descricao": "Nova Caixa",
            "morador": self.morador.id,
            "unidade": self.unidade.id,
            "entregue_por": "Sedex",
            "observacoes": "Contém eletrônicos"
        }
        response = self.client.post('/api/correspondencias/', dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['descricao'], dados['descricao'])

    def test_listar_correspondencias(self):
        """Testa a listagem de correspondências"""
        response = self.client.get('/api/correspondencias/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # DRF usa paginação por padrão
        self.assertIn('results', response.data)
        self.assertGreaterEqual(len(response.data['results']), 1)

    def test_atualizar_correspondencia(self):
        """Testa a atualização de uma correspondência"""
        novos_dados = {
            "descricao": "Atualizada",
            "morador": self.morador.id,
            "unidade": self.unidade.id,
            "entregue_por": "Transportadora",
            "data_retirada": "2025-04-10T20:00:00Z",
            "observacoes": "Atualizada"
        }
        response = self.client.put(
            f'/api/correspondencias/{self.correspondencia.id}/',
            novos_dados,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # verifica que retornou a data de retirada
        self.assertIsNotNone(response.data.get('data_retirada'))

    def test_deletar_correspondencia(self):
        """Testa a exclusão de uma correspondência"""
        response = self.client.delete(f'/api/correspondencias/{self.correspondencia.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Correspondencia.objects.filter(id=self.correspondencia.id).exists())

    def test_filtrar_por_morador(self):
        """Testa filtro por morador"""
        response = self.client.get(f'/api/correspondencias/?morador={self.morador.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(response.data.get('count', 0), 1)
        for item in response.data['results']:
            self.assertEqual(item['morador'], self.morador.id)

    def test_filtrar_por_unidade(self):
        """Testa filtro por unidade"""
        response = self.client.get(f'/api/correspondencias/?unidade={self.unidade.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(response.data.get('count', 0), 1)
        for item in response.data['results']:
            self.assertEqual(item['unidade'], self.unidade.id)

    def test_filtrar_por_entregue_por(self):
        """Testa filtro por entregador"""
        response = self.client.get('/api/correspondencias/?entregue_por=Correios')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(response.data.get('count', 0), 1)
        for item in response.data['results']:
            self.assertEqual(item['entregue_por'], "Correios")
