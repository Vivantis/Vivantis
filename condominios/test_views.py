from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from condominios.models import Condominio

class CondominioAPITests(APITestCase):
    """
    Testes automatizados para os endpoints da API de Condomínios.
    Inclui criação, listagem, atualização e remoção de dados.
    """

    def setUp(self):
        """
        Preparação inicial antes de cada teste.
        Cria um usuário, obtém o token JWT e configura o cabeçalho de autenticação.
        """
        # Criação de um usuário para autenticação
        self.user = User.objects.create_user(username='admin', password='admin123')

        # Requisição de token JWT via endpoint /api/token/
        response = self.client.post(reverse('token_obtain_pair'), {
            'username': 'admin',
            'password': 'admin123'
        }, format='json')

        # Extrai o token de acesso do JSON de resposta
        token = response.data['access']

        # Define o cabeçalho de autorização com o token JWT
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        # Define a URL base da API de condomínios
        self.url = reverse('condominio-list')

        # Dados de exemplo usados nos testes
        self.dados = {
            'nome': 'Residencial Nova Era',
            'endereco': 'Rua das Flores, 123'
        }

    def test_criar_condominio(self):
        """
        Testa a criação de um novo condomínio via POST.
        """
        response = self.client.post(self.url, self.dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Condominio.objects.count(), 1)

    def test_listar_condominios(self):
        """
        Testa a listagem dos condomínios via GET.
        """
        Condominio.objects.create(**self.dados)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_atualizar_condominio(self):
        """
        Testa a atualização dos dados de um condomínio via PUT.
        """
        cond = Condominio.objects.create(**self.dados)
        url = reverse('condominio-detail', args=[cond.id])
        novos_dados = {
            'nome': 'Residencial Atualizado',
            'endereco': 'Rua Nova, 456'
        }
        response = self.client.put(url, novos_dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        cond.refresh_from_db()
        self.assertEqual(cond.nome, 'Residencial Atualizado')

    def test_deletar_condominio(self):
        """
        Testa a exclusão de um condomínio via DELETE.
        """
        cond = Condominio.objects.create(**self.dados)
        url = reverse('condominio-detail', args=[cond.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Condominio.objects.count(), 0)
