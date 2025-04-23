from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from condominios.perfil.models import PerfilUsuario

class PerfilUsuarioTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='vitor', password='123456', email='vitor@teste.com')
        self.user2 = User.objects.create_user(username='outro', password='123456', email='outro@teste.com')
        self.perfil = PerfilUsuario.objects.create(user=self.user, telefone='11999999999', bio='Dev Top')
        self.perfil2 = PerfilUsuario.objects.create(user=self.user2, telefone='11888888888', bio='Outro Dev')
        self.client.login(username='vitor', password='123456')

    def test_listar_perfil_proprio(self):
        response = self.client.get('/api/perfil/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['user'], self.user.id)

    def test_nao_ver_perfil_de_outra_pessoa(self):
        # Tentando acessar diretamente o perfil de outro user
        response = self.client.get(f'/api/perfil/{self.perfil2.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_editar_proprio_perfil(self):
        payload = {'bio': 'Atualizado via teste'}
        response = self.client.patch(f'/api/perfil/{self.perfil.id}/', payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.perfil.refresh_from_db()
        self.assertEqual(self.perfil.bio, 'Atualizado via teste')

    def test_editar_perfil_de_outra_pessoa(self):
        payload = {'bio': 'Tentativa não autorizada'}
        response = self.client.patch(f'/api/perfil/{self.perfil2.id}/', payload)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

