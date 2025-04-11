from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import PerfilUsuario

class PerfilUsuarioAPITests(APITestCase):
    """
    Testes para o endpoint /api/perfil/ que permite visualizar e atualizar os dados do perfil do usuário.
    """

    def setUp(self):
        # Cria um usuário e autentica
        self.user = User.objects.create_user(username='vitor', email='vitor@email.com', password='123456')
        self.client.force_authenticate(user=self.user)

    def test_criar_perfil_automaticamente(self):
        """Testa se o perfil é criado automaticamente ao acessar a rota"""
        response = self.client.get('/api/perfil/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)

        # Confirma que o perfil foi criado no banco
        self.assertTrue(PerfilUsuario.objects.filter(user=self.user).exists())

    def test_atualizar_dados_do_perfil(self):
        """Testa a edição de dados do perfil (telefone e bio)"""
        payload = {
            "telefone": "(11) 91234-5678",
            "bio": "Desenvolvedor do projeto Vivantis"
        }

        response = self.client.put('/api/perfil/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['telefone'], payload['telefone'])
        self.assertEqual(response.data['bio'], payload['bio'])

        perfil = PerfilUsuario.objects.get(user=self.user)
        self.assertEqual(perfil.telefone, payload['telefone'])
        self.assertEqual(perfil.bio, payload['bio'])
