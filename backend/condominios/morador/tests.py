from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from condominios.condominio.models import Condominio
from condominios.unidade.models import Unidade
from condominios.morador.models import Morador
from condominios.administradorgeral.models import AdministradorGeral


class MoradorAPITests(APITestCase):
    """
    Testes para os endpoints de Morador
    """

    def setUp(self):
        # Cria e autentica um usuário administrador geral (síndico)
        self.user = User.objects.create_user(username="admin", password="admin123")
        AdministradorGeral.objects.create(
            user=self.user,
            nome="Admin Teste",
            telefone="11999999999"
        )
        self.client.force_authenticate(user=self.user)

        # Cria um condomínio válido
        self.condominio = Condominio.objects.create(
            nome="Condomínio Sol",
            endereco="Rua Central, 123",
            cidade="São Paulo",
            estado="SP",
            ativo=True
        )

        # Cria uma unidade e um morador inicial
        self.unidade = Unidade.objects.create(
            numero="101",
            bloco="A",
            condominio=self.condominio
        )
        self.morador = Morador.objects.create(
            nome="João Silva",
            email="joao@email.com",
            unidade=self.unidade
        )

    def test_criar_morador(self):
        """Testa a criação de um novo morador via POST"""
        dados = {
            "nome": "Maria Oliveira",
            "email": "maria@email.com",
            "unidade": self.unidade.id
        }
        response = self.client.post("/api/moradores/", dados, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["nome"], dados["nome"])
        self.assertEqual(response.data["unidade"], self.unidade.id)

    def test_listar_moradores(self):
        """Testa a listagem de moradores via GET"""
        # Deve retornar pelo menos o João já criado no setUp
        response = self.client.get("/api/moradores/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("count", response.data)
        self.assertIn("results", response.data)
        self.assertGreaterEqual(response.data["count"], 1)
        self.assertIsInstance(response.data["results"], list)

    def test_atualizar_morador(self):
        """Testa edição de dados do morador via PUT"""
        novos_dados = {
            "nome": "João Atualizado",
            "email": "joao_novo@email.com",
            "unidade": self.unidade.id
        }
        response = self.client.put(f"/api/moradores/{self.morador.id}/", novos_dados, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["nome"], novos_dados["nome"])
        self.assertEqual(response.data["email"], novos_dados["email"])

    def test_deletar_morador(self):
        """Testa exclusão de morador via DELETE"""
        response = self.client.delete(f"/api/moradores/{self.morador.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Morador.objects.filter(id=self.morador.id).exists())

    def test_filtrar_moradores_por_nome(self):
        """Testa filtragem de moradores por nome"""
        # Adiciona mais registros
        Unidade.objects.create(numero="102", bloco="B", condominio=self.condominio)
        Morador.objects.create(nome="Maria Silva", email="maria@email.com", unidade=self.unidade)
        response = self.client.get("/api/moradores/?nome=Maria")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        nomes = [m["nome"] for m in response.data["results"]]
        self.assertIn("Maria Silva", nomes)

    def test_filtrar_moradores_por_email(self):
        """Testa filtragem de moradores por email"""
        Morador.objects.create(nome="Carlos Lima", email="carlos@email.com", unidade=self.unidade)
        response = self.client.get("/api/moradores/?email=carlos@email.com")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        emails = [m["email"] for m in response.data["results"]]
        self.assertIn("carlos@email.com", emails)

    def test_filtrar_moradores_por_unidade(self):
        """Testa filtragem de moradores por ID de unidade"""
        # Já há ao menos um morador em self.unidade
        response = self.client.get(f"/api/moradores/?unidade={self.unidade.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        unidades = [m["unidade"] for m in response.data["results"]]
        self.assertTrue(all(u == self.unidade.id for u in unidades))
