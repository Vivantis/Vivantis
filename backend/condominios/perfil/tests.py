from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

from condominios.perfil.models import PerfilUsuario


class PerfilUsuarioTests(APITestCase):
    """
    Testes para o endpoint de Perfil do Usuário:
    - Listagem deve retornar apenas o perfil do usuário autenticado
    - Acesso e edição de outros perfis devem ser proibidos
    """

    def setUp(self):
        # Cria dois usuários e seus perfis
        self.user = User.objects.create_user(
            username='vitor', password='123456', email='vitor@teste.com'
        )
        self.user2 = User.objects.create_user(
            username='outro', password='123456', email='outro@teste.com'
        )

        self.perfil = PerfilUsuario.objects.create(
            user=self.user, telefone='11999999999', bio='Dev Top'
        )
        self.perfil2 = PerfilUsuario.objects.create(
            user=self.user2, telefone='11888888888', bio='Outro Dev'
        )

        # Autentica como o primeiro usuário
        self.client.login(username='vitor', password='123456')

    def test_listar_perfil_proprio(self):
        """GET /api/perfil/ deve retornar apenas o perfil do usuário logado"""
        response = self.client.get('/api/perfil/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['user'], self.user.id)

    def test_nao_ver_perfil_de_outra_pessoa(self):
        """GET /api/perfil/<id>/ de outro usuário deve ser 403"""
        response = self.client.get(f'/api/perfil/{self.perfil2.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_editar_proprio_perfil(self):
        """PATCH /api/perfil/<own_id>/ deve permitir atualizar apenas seu perfil"""
        payload = {'bio': 'Atualizado via teste'}
        response = self.client.patch(f'/api/perfil/{self.perfil.id}/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.perfil.refresh_from_db()
        self.assertEqual(self.perfil.bio, payload['bio'])

    def test_editar_perfil_de_outra_pessoa(self):
        """PATCH /api/perfil/<other_id>/ deve retornar 403 Forbidden"""
        payload = {'bio': 'Tentativa não autorizada'}
        response = self.client.patch(f'/api/perfil/{self.perfil2.id}/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
