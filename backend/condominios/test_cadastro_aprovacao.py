from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class CadastroAprovacaoUsuarioTests(APITestCase):
    def test_cadastro_usuario_aguardando_aprovacao(self):
        """
        Testa se um novo usuário é criado com is_active=False
        """
        url = reverse('cadastro-usuario')
        data = {
            'username': 'usuario_teste',
            'email': 'teste@example.com',
            'password': 'senhaSegura123'
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verifica se o usuário foi criado e está inativo
        user = User.objects.get(username='usuario_teste')
        self.assertFalse(user.is_active)

    def test_aprovar_usuario_por_admin(self):
        """
        Testa se um superusuário pode aprovar (ativar) um usuário pendente
        """
        # Cria um usuário pendente (inativo)
        user_pendente = User.objects.create_user(
            username='pendente', email='pendente@example.com', password='teste123', is_active=False
        )

        # Cria um superusuário e autentica com ele
        admin = User.objects.create_superuser(
            username='admin', email='admin@example.com', password='admin123'
        )
        self.client.force_authenticate(user=admin)

        url = reverse('aprovar-usuario', kwargs={'pk': user_pendente.pk})
        response = self.client.patch(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verifica se o usuário foi ativado
        user_pendente.refresh_from_db()
        self.assertTrue(user_pendente.is_active)

