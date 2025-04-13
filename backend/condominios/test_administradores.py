from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from condominios.models import AdministradorGeral


class AdministradorGeralAPITests(APITestCase):
    """
    Testes automatizados para a API de Administradores Gerais
    """

    def setUp(self):
        # Cria um administrador autenticado para os testes
        self.user = User.objects.create_user(username='admin_geral', password='admin123')
        self.admin_profile = AdministradorGeral.objects.create(user=self.user, nome='Admin', telefone='(11) 90000-0000')
        self.client.force_authenticate(user=self.user)

    def test_criar_administrador(self):
        """Testa a criação de um administrador geral"""
        novo_user = User.objects.create_user(username='novo_admin', password='123456')
        dados = {
            "user": novo_user.id,
            "nome": "Gestor Regional",
            "telefone": "(11) 99999-0000"
        }
        response = self.client.post('/api/administradores/', dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nome'], dados['nome'])

    def test_listar_administradores(self):
        """Testa a listagem de administradores existentes"""
        outro_user = User.objects.create_user(username='zelador_pro', password='123456')
        AdministradorGeral.objects.create(user=outro_user, nome="Zelador Pro", telefone="(11) 90000-0000")

        response = self.client.get('/api/administradores/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_editar_administrador(self):
        """Testa a atualização dos dados de um administrador"""
        outro_user = User.objects.create_user(username='fulano', password='123456')
        adm = AdministradorGeral.objects.create(user=outro_user, nome="Fulano", telefone="(11) 90000-1234")

        novos_dados = {
            "user": outro_user.id,
            "nome": "Fulano Atualizado",
            "telefone": "(11) 95555-0000"
        }
        response = self.client.put(f'/api/administradores/{adm.id}/', novos_dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], "Fulano Atualizado")

    def test_deletar_administrador(self):
        """Testa a exclusão de um administrador"""
        outro_user = User.objects.create_user(username='deletavel', password='123456')
        adm = AdministradorGeral.objects.create(user=outro_user, nome="Deletável", telefone="(11) 90000-1234")

        response = self.client.delete(f'/api/administradores/{adm.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(AdministradorGeral.objects.filter(id=adm.id).exists())
