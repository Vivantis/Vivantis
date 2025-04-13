from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Condominio, Unidade, Morador, Correspondencia


class CorrespondenciaAPITests(APITestCase):
    """
    Testes automatizados para a API de Correspondências
    """

    def setUp(self):
        # Cria e autentica um usuário
        self.user = User.objects.create_user(username='admin', password='admin123')
        self.client.force_authenticate(user=self.user)

        # Cria dados relacionados
        self.condominio = Condominio.objects.create(nome="Condomínio Nova Era", endereco="Av. Central, 456")
        self.unidade = Unidade.objects.create(numero="302", bloco="C", condominio=self.condominio)
        self.morador = Morador.objects.create(nome="Carlos Morador", email="carlos@example.com", unidade=self.unidade)

        # Dados padrão para envio via API
        self.dados = {
            "descricao": "Encomenda da Amazon",
            "morador": self.morador.id,
            "unidade": self.unidade.id,
            "entregue_por": "Correios",
            "observacoes": "Caixa pequena"
        }

    def test_criar_correspondencia(self):
        """Testa a criação de uma nova correspondência"""
        response = self.client.post('/api/correspondencias/', self.dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['descricao'], self.dados['descricao'])

    def test_listar_correspondencias(self):
        """Testa a listagem de correspondências"""
        Correspondencia.objects.create(
            descricao="Carta registrada",
            morador=self.morador,
            unidade=self.unidade,
            entregue_por="Correios",
            observacoes="Urgente"
        )
        response = self.client.get('/api/correspondencias/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_atualizar_correspondencia(self):
        """Testa a atualização de uma correspondência (ex: marcar retirada)"""
        correspondencia = Correspondencia.objects.create(
            descricao="Encomenda Shopee",
            morador=self.morador,
            unidade=self.unidade
        )
        novos_dados = {
            "descricao": "Encomenda Shopee",
            "morador": self.morador.id,
            "unidade": self.unidade.id,
            "entregue_por": "Transportadora",
            "data_retirada": "2025-04-10T20:00:00Z",
            "observacoes": "Retirada às 20h"
        }
        response = self.client.put(f'/api/correspondencias/{correspondencia.id}/', novos_dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data['data_retirada'])

    def test_deletar_correspondencia(self):
        """Testa a exclusão de uma correspondência"""
        correspondencia = Correspondencia.objects.create(
            descricao="Revista Exame",
            morador=self.morador,
            unidade=self.unidade
        )
        response = self.client.delete(f'/api/correspondencias/{correspondencia.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Correspondencia.objects.filter(id=correspondencia.id).exists())
