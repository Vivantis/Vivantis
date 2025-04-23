from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

class CadastroAprovacaoTests(APITestCase):

    def test_cadastrar_usuario(self):
        data = {
            'username': 'novo_user',
            'email': 'novo@teste.com',
            'password': 'senha123'
        }
        response = self.client.post('/api/usuarios/cadastro/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertFalse(User.objects.get(username='novo_user').is_active)

    def test_aprovar_usuario(self):
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.client.login(username='admin', password='admin123')
        user = User.objects.create_user(username='usuario1', email='u1@teste.com', password='teste', is_active=False)
        response = self.client.patch(f'/api/usuarios/aprovar/{user.id}/', {'is_active': True})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user.refresh_from_db()
        self.assertTrue(user.is_active)
