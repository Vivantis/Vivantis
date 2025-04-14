from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class CadastroAprovacaoUsuarioTests(APITestCase):
    """
    Testes automatizados para o fluxo de cadastro e aprovação de usuários
    """

    def test_cadastro_usuario_aguardando_aprovacao(self):
        """
        Testa se um novo usuário é criado com is_active=False
        """
        url = reverse('cadastro-usuario')
        dados = {
            'username': 'usuario_teste',
            'email': 'teste@example.com',
            'password': 'senhaSegura123'
        }

        response = self.client.post(url, dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verifica se o usuário foi criado corretamente
        self.assertTrue(User.objects.filter(username='usuario_teste').exists())
        usuario = User.objects.get(username='usuario_teste')
        self.assertFalse(usuario.is_active)

    def test_aprovar_usuario_por_admin(self):
        """
        Testa se um superusuário pode aprovar (ativar) um usuário pendente
        """
        # Cria um usuário inativo para ser aprovado
        usuario_pendente = User.objects.create_user(
            username='pendente',
            email='pendente@example.com',
            password='teste123',
            is_active=False
        )

        # Cria um superusuário e autentica a requisição
        admin = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123'
        )
        self.client.force_authenticate(user=admin)

        url = reverse('aprovar-usuario', kwargs={'pk': usuario_pendente.pk})
        response = self.client.patch(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        usuario_pendente.refresh_from_db()
        self.assertTrue(usuario_pendente.is_active)

    def test_aprovar_usuario_ja_ativo(self):
        """
        Testa se o sistema impede a reaprovação de um usuário já ativo
        """
        usuario_ativo = User.objects.create_user(
            username='jaativo',
            email='jaativo@example.com',
            password='senha123',
            is_active=True
        )

        admin = User.objects.create_superuser(
            username='admin2',
            email='admin2@example.com',
            password='admin123'
        )
        self.client.force_authenticate(user=admin)

        url = reverse('aprovar-usuario', kwargs={'pk': usuario_ativo.pk})
        response = self.client.patch(url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('já está ativo', response.data['detail'])

    def test_aprovar_usuario_comum_deve_falhar(self):
        """
        Testa se um usuário comum não pode aprovar usuários
        """
        user_comum = User.objects.create_user(
            username='comum',
            email='comum@example.com',
            password='senha123'
        )
        self.client.force_authenticate(user=user_comum)

        usuario_pendente = User.objects.create_user(
            username='pendente2',
            email='pendente2@example.com',
            password='teste123',
            is_active=False
        )

        url = reverse('aprovar-usuario', kwargs={'pk': usuario_pendente.pk})
        response = self.client.patch(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
