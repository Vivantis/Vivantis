from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from condominios.condominio.models import Condominio


class CondominioAPITests(APITestCase):
    """
    Testes para os endpoints de Condomínio
    """

    def setUp(self):
        # Usuário autenticado
        self.user = User.objects.create_user(username="admin", password="admin123")
        self.client.force_authenticate(user=self.user)

        # Cria um condomínio base para os testes
        self.condominio = Condominio.objects.create(
            nome="Residencial Primavera",
            endereco="Rua A, 123",
            cidade="São Paulo",
            estado="SP",
            ativo=True
        )

    def test_criar_condominio(self):
        """Testa a criação de um novo condomínio via POST."""
        dados = {
            "nome": "Residencial Novo Horizonte",
            "endereco": "Avenida das Palmeiras, 456",
            "cidade": "Campinas",
            "estado": "SP",
            "ativo": True
        }
        response = self.client.post("/api/condominios/", dados, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["nome"], dados["nome"])

    def test_listar_condominios(self):
        """Testa a listagem dos condomínios via GET."""
        response = self.client.get("/api/condominios/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # verifica paginação DRF padrão
        self.assertIn("results", response.data)
        self.assertGreaterEqual(len(response.data["results"]), 1)

    def test_atualizar_condominio(self):
        """Testa a atualização dos dados de um condomínio via PUT."""
        novos_dados = {
            "nome": "Residencial Atualizado",
            "endereco": "Rua B, 321",
            "cidade": "São Paulo",
            "estado": "SP",
            "ativo": True
        }
        response = self.client.put(
            f"/api/condominios/{self.condominio.id}/",
            novos_dados,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["nome"], "Residencial Atualizado")

    def test_deletar_condominio(self):
        """Testa a exclusão de um condomínio via DELETE."""
        response = self.client.delete(f"/api/condominios/{self.condominio.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Condominio.objects.filter(id=self.condominio.id).exists())

    def test_filtrar_condominios_por_cidade(self):
        """Testa o filtro por cidade na listagem."""
        response = self.client.get("/api/condominios/?cidade=São Paulo")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # garante que ao menos um item retornado tem cidade "São Paulo"
        self.assertTrue(any(c["cidade"] == "São Paulo" for c in response.data["results"]))

    def test_buscar_condominio_por_nome(self):
        """Testa a busca por nome parcial via ?search=""."""
        response = self.client.get("/api/condominios/?search=Primavera")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Primavera" in c["nome"] for c in response.data["results"]))

    def test_ordenar_condominios_por_nome(self):
        """Testa a ordenação dos condomínios por nome."""
        Condominio.objects.create(
            nome="Alphaville Central",
            endereco="Rua Z",
            cidade="Barueri",
            estado="SP",
            ativo=True
        )
        response = self.client.get("/api/condominios/?ordering=nome")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        nomes = [c["nome"] for c in response.data["results"]]
        self.assertEqual(nomes, sorted(nomes))
