from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from condominios.models import Condominio, Unidade, Morador


class MoradorAPITests(APITestCase):
    """
    Testes para os endpoints de Morador
    """

    def setUp(self):
        self.user = User.objects.create_user(username="admin", password="admin123")
        self.client.force_authenticate(user=self.user)

        self.condominio = Condominio.objects.create(nome="Condomínio Sol", endereco="Rua Central, 123")
        self.unidade = Unidade.objects.create(numero="101", bloco="A", condominio=self.condominio)

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

    def test_listar_moradores(self):
        """Testa a listagem de moradores via GET"""
        response = self.client.get("/api/moradores/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_atualizar_morador(self):
        """Testa edição de dados do morador via PUT"""
        novos_dados = {
            "nome": "João Atualizado",
            "email": "joao_novo@email.com",
            "unidade": self.unidade.id
        }
        response = self.client.put(f"/api/moradores/{self.morador.id}/", novos_dados, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["nome"], "João Atualizado")

    def test_deletar_morador(self):
        """Testa exclusão de morador via DELETE"""
        response = self.client.delete(f"/api/moradores/{self.morador.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Morador.objects.filter(id=self.morador.id).exists())


def test_filtrar_moradores_por_nome_email_unidade(self):
    """
    Testa filtragem de moradores por nome, email e unidade
    """
    # Morador adicional para teste de filtragem
    unidade2 = Unidade.objects.create(numero="102", bloco="B", condominio=self.condominio)
    morador1 = Morador.objects.create(nome="Maria Silva", email="maria@email.com", unidade=unidade2)
    morador2 = Morador.objects.create(nome="Carlos Lima", email="carlos@email.com", unidade=self.unidade)

    # Filtrar por nome
    response = self.client.get('/api/moradores/?nome=Maria')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertTrue(any("Maria" in m["nome"] for m in response.data))

    # Filtrar por email
    response = self.client.get('/api/moradores/?email=carlos@email.com')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data[0]['email'], 'carlos@email.com')

    # Filtrar por unidade (usando ID)
    response = self.client.get(f'/api/moradores/?unidade={self.unidade.id}')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertTrue(all(m['unidade'] == self.unidade.id for m in response.data))
