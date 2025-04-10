from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import AdministradorGeral


class AdministradorGeralAPITests(APITestCase):
    """
    Testes automatizados para a API de Administradores Gerais
    """

    def setUp(self):
        # Cria e autentica um usuário comum (que será um administrador geral)
        self.user = User.objects.create_user(username='admin_geral', password='admin123')
        self.client.force_authenticate(user=self.user)

        # Dados padrão para criação de administrador geral
        self.dados = {
            "user": self.user.id,
            "nome": "Gestor Regional",
            "telefone": "(11) 99999-0000"
        }

    def test_criar_administrador(self):
        """Testa a criação de um administrador geral"""
        response = self.client.post('/api/administradores/', self.dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nome'], self.dados['nome'])

    def test_listar_administradores(self):
        """Testa a listagem de administradores existentes"""
        AdministradorGeral.objects.create(user=self.user, nome="Zelador Pro", telefone="(11) 90000-0000")
        response = self.client.get('/api/administradores/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_editar_administrador(self):
        """Testa a atualização dos dados de um administrador"""
        adm = AdministradorGeral.objects.create(user=self.user, nome="Fulano", telefone="(11) 90000-1234")
        novos_dados = {
            "user": self.user.id,
            "nome": "Fulano Atualizado",
            "telefone": "(11) 95555-0000"
        }
        response = self.client.put(f'/api/administradores/{adm.id}/', novos_dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], "Fulano Atualizado")

    def test_deletar_administrador(self):
        """Testa a exclusão de um administrador"""
        adm = AdministradorGeral.objects.create(user=self.user, nome="Deletável", telefone="(11) 90000-1234")
        response = self.client.delete(f'/api/administradores/{adm.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(AdministradorGeral.objects.filter(id=adm.id).exists())

