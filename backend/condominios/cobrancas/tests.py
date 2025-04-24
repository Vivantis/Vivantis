import pytest
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.utils import timezone

from condominios.cobrancas.models import Cobranca
from condominios.condominio.models import Condominio
from condominios.unidade.models import Unidade
from condominios.morador.models import Morador
from condominios.administradorgeral.models import AdministradorGeral

@pytest.mark.django_db
class CobrancaAPITests(APITestCase):
    """
    Testes para o CRUD e filtros do endpoint /api/cobrancas/
    """

    def setUp(self):
        # Cria usuário e perfil administrativo
        self.user = User.objects.create_user(username='admin', password='admin123')
        AdministradorGeral.objects.create(
            user=self.user,
            nome="Administrador",
            telefone="(11) 99999-9999"
        )
        self.client.force_authenticate(user=self.user)

        # Dados básicos de condomínio, unidade e morador
        self.condominio = Condominio.objects.create(
            nome="Condomínio Sol",
            endereco="Rua Teste, 123"
        )
        self.unidade = Unidade.objects.create(
            numero="101",
            bloco="A",
            condominio=self.condominio
        )
        self.morador = Morador.objects.create(
            nome="Carlos",
            email="carlos@email.com",
            unidade=self.unidade
        )

        # Payload JSON para a API
        today = timezone.now().date()
        self.payload = {
            "unidade": self.unidade.id,
            "morador": self.morador.id,
            "tipo": "mensalidade",
            "descricao": "Cobrança de Abril",
            "valor": "300.00",
            "vencimento": str(today),
            "status": "pendente"
        }

        # Dados para criar direto via ORM
        self.model_data = {
            "unidade": self.unidade,
            "morador": self.morador,
            "tipo": "mensalidade",
            "descricao": "Cobrança de Abril",
            "valor": "300.00",
            "vencimento": today,
            "status": "pendente"
        }

    def test_criar_cobranca(self):
        response = self.client.post("/api/cobrancas/", self.payload, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["descricao"] == self.payload["descricao"]

    def test_listar_cobrancas(self):
        Cobranca.objects.create(**self.model_data)
        response = self.client.get("/api/cobrancas/")
        assert response.status_code == status.HTTP_200_OK
        # paginação DRF padrão
        assert response.data["count"] >= 1
        assert isinstance(response.data["results"], list)

    def test_atualizar_cobranca(self):
        cobranca = Cobranca.objects.create(**self.model_data)
        novos = self.payload.copy()
        novos.update({"descricao": "Atualizado", "status": "pago"})
        response = self.client.put(f"/api/cobrancas/{cobranca.id}/", novos, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["status"] == "pago"

    def test_deletar_cobranca(self):
        cobranca = Cobranca.objects.create(**self.model_data)
        response = self.client.delete(f"/api/cobrancas/{cobranca.id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Cobranca.objects.filter(id=cobranca.id).exists()

    def test_filtrar_por_status(self):
        Cobranca.objects.create(**self.model_data)
        response = self.client.get("/api/cobrancas/?status=pendente")
        assert response.status_code == status.HTTP_200_OK
        for item in response.data["results"]:
            assert item["status"] == "pendente"

    def test_filtrar_por_morador(self):
        Cobranca.objects.create(**self.model_data)
        response = self.client.get(f"/api/cobrancas/?morador={self.morador.id}")
        assert response.status_code == status.HTTP_200_OK
        for item in response.data["results"]:
            assert item["morador"] == self.morador.id

    def test_filtrar_por_tipo(self):
        Cobranca.objects.create(**self.model_data)
        response = self.client.get("/api/cobrancas/?tipo=mensalidade")
        assert response.status_code == status.HTTP_200_OK
        for item in response.data["results"]:
            assert item["tipo"] == "mensalidade"
