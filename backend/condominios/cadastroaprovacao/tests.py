from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

class CadastroAprovacaoTests(APITestCase):
    """
    Testes para o fluxo de cadastro (inativo) e aprovação de usuários.
    """

    def test_cadastrar_usuario(self):
        """Ao cadastrar, o usuário deve ser criado mas ficar inativo."""
        data = {
            "username": "novo_user",
            "email": "novo@teste.com",
            "password": "senha123"
        }
        response = self.client.post("/api/usuarios/cadastro/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user = User.objects.get(username="novo_user")
        self.assertFalse(user.is_active)

    def test_aprovar_usuario(self):
        """Apenas um admin consegue ativar o usuário."""
        # Cria e autentica superuser
        admin = User.objects.create_superuser(
            username="admin", email="admin@admin.com", password="admin123"
        )
        self.client.force_authenticate(user=admin)

        # Cria usuário inativo
        user = User.objects.create_user(
            username="usuario1", email="u1@teste.com", password="teste", is_active=False
        )

        # Aprova (ativa) via PATCH
        response = self.client.patch(
            f"/api/usuarios/aprovar/{user.id}/",
            {"is_active": True},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user.refresh_from_db()
        self.assertTrue(user.is_active)
