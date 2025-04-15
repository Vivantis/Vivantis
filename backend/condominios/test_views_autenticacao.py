from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status


class AutenticacaoUsuarioTestCase(APITestCase):
    """
    Testa o fluxo completo de autenticação e aprovação de usuário via JWT
    """

    def setUp(self):
        # Cria um usuário administrador para aprovar novos usuários
        self.admin = User.objects.create_user(
            username="admin_test",
            password="admin123",
            is_staff=True,
            is_superuser=True
        )

        # Dados do usuário que será cadastrado
        self.dados_usuario = {
            "username": "usuario_teste",
            "email": "teste@exemplo.com",
            "password": "senha123"
        }

    def test_fluxo_completo_de_autenticacao(self):
        # 🔹 1. Cadastra um novo usuário (inativo por padrão)
        response_cadastro = self.client.post("/api/usuarios/cadastro/", self.dados_usuario)
        self.assertEqual(response_cadastro.status_code, status.HTTP_201_CREATED)
        user_id = response_cadastro.data.get("id")
        self.assertIsNotNone(user_id)

        # 🔹 2. Faz login como admin e obtém o token JWT
        response_token = self.client.post("/api/token/", {
            "username": "admin_test",
            "password": "admin123"
        })
        self.assertEqual(response_token.status_code, status.HTTP_200_OK)
        token = response_token.data["access"]
        self.assertTrue(token)

        # 🔹 3. Usa o token para autenticar e aprovar o novo usuário
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        response_aprovacao = self.client.patch(f"/api/usuarios/cadastro/aprovar/{user_id}/")
        self.assertEqual(response_aprovacao.status_code, status.HTTP_200_OK)
        self.assertEqual(response_aprovacao.data["detail"], "Usuário aprovado com sucesso.")
