from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from condominios.models import Condominio, Unidade, Morador

class MoradorAPITests(APITestCase):
    """
    Testes automatizados para os endpoints da API de Moradores.
    """

    def setUp(self):
        # Criação de usuário e autenticação JWT
        self.user = User.objects.create_user(username='admin', password='admin123')

        # Gera token de acesso
        response = self.client.post(reverse('token_obtain_pair'), {
            'username': 'admin',
            'password': 'admin123'
        }, format='json')
        token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        # Criar dados base: condomínio e unidade vinculada
        self.condominio = Condominio.objects.create(nome='Vivantis Luxo', endereco='Rua Central, 123')
        self.unidade = Unidade.objects.create(numero='101', bloco='A', condominio=self.condominio)

        # Dados para POST (usado pela API — pode conter o ID)
        self.dados = {
            'nome': 'João Oliveira',
            'email': 'joao@email.com',
            'unidade': self.unidade.id  # Aqui usamos o ID porque vai ser passado via JSON
        }

        self.url = reverse('morador-list')

    def test_criar_morador(self):
        """Testa a criação de um novo morador via POST"""
        response = self.client.post(self.url, self.dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Morador.objects.count(), 1)

    def test_listar_moradores(self):
        """Testa a listagem de moradores via GET"""
        # Aqui usamos o objeto Unidade (não o ID), pois estamos criando direto no banco
        Morador.objects.create(nome='Maria', email='maria@email.com', unidade=self.unidade)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_atualizar_morador(self):
        """Testa edição de dados do morador via PUT"""
        morador = Morador.objects.create(nome='Lucas', email='lucas@email.com', unidade=self.unidade)
        url = reverse('morador-detail', args=[morador.id])
        novos_dados = {
            'nome': 'Lucas Atualizado',
            'email': 'lucasnovo@email.com',
            'unidade': self.unidade.id  # Aqui pode ser ID, pois é via API
        }
        response = self.client.put(url, novos_dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        morador.refresh_from_db()
        self.assertEqual(morador.nome, 'Lucas Atualizado')

    def test_deletar_morador(self):
        """Testa exclusão de morador via DELETE"""
        morador = Morador.objects.create(nome='Ana', email='ana@email.com', unidade=self.unidade)
        url = reverse('morador-detail', args=[morador.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Morador.objects.count(), 0)
