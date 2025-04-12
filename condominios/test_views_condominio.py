from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from condominios.models import Condominio


class CondominioAPITests(APITestCase):
    """
    Testes para os endpoints de Condomínio
    """

    def setUp(self):
        self.user = User.objects.create_user(username="admin", password="admin123")
        self.client.force_authenticate(user=self.user)

        self.condominio = Condominio.objects.create(
            nome="Residencial Primavera", endereco="Rua A, 123"
        )

    def test_criar_condominio(self):
        """Testa a criação de um novo condomínio via POST."""
        dados = {
            "nome": "Residencial Novo Horizonte",
            "endereco": "Avenida das Palmeiras, 456"
        }
        response = self.client.post("/api/condominios/", dados, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["nome"], dados["nome"])

    def test_listar_condominios(self):
        """Testa a listagem dos condomínios via GET."""
        response = self.client.get("/api/condominios/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_atualizar_condominio(self):
        """Testa a atualização dos dados de um condomínio via PUT."""
        novos_dados = {
            "nome": "Residencial Atualizado",
            "endereco": "Rua B, 321"
        }
        response = self.client.put(f"/api/condominios/{self.condominio.id}/", novos_dados, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["nome"], "Residencial Atualizado")

    def test_deletar_condominio(self):
        """Testa a exclusão de um condomínio via DELETE."""
        response = self.client.delete(f"/api/condominios/{self.condominio.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Condominio.objects.filter(id=self.condominio.id).exists())
