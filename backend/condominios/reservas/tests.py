from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

from condominios.condominio.models import Condominio
from condominios.unidade.models import Unidade
from condominios.morador.models import Morador
from condominios.espacoscomuns.models import EspacoComum
from condominios.reservas.models import ReservaEspaco


class ReservaEspacoAPITests(APITestCase):
    """
    Testes automatizados para a API de Reservas de Espaços
    """

    def setUp(self):
        # usuário administrador e autenticação
        self.user = User.objects.create_user(username='admin', password='admin123')
        self.client.force_authenticate(user=self.user)

        # dados básicos
        self.condominio = Condominio.objects.create(
            nome="Condomínio Reserva", endereco="Rua das Reservas, 789"
        )
        self.unidade = Unidade.objects.create(
            numero="101", bloco="A", condominio=self.condominio
        )
        self.morador = Morador.objects.create(
            nome="Maria Reservadora",
            email="maria@exemplo.com",
            unidade=self.unidade
        )
        self.espaco = EspacoComum.objects.create(
            nome="Salão de Festas", condominio=self.condominio
        )

        # payload usado pela API (IDs)
        self.payload = {
            "morador": self.morador.id,
            "unidade": self.unidade.id,
            "espaco": self.espaco.id,
            "data": "2025-04-20",
            "horario_inicio": "14:00",
            "horario_fim": "18:00",
            "status": "pendente",
            "observacoes": "Festa de aniversário",
        }

        # dados para criar direto no banco (instâncias)
        self.model_data = {
            "morador": self.morador,
            "unidade": self.unidade,
            "espaco": self.espaco,
            "data": self.payload["data"],
            "horario_inicio": self.payload["horario_inicio"],
            "horario_fim": self.payload["horario_fim"],
            "status": self.payload["status"],
            "observacoes": self.payload["observacoes"],
        }

    def test_criar_reserva(self):
        """POST /api/reservas/ deve criar uma reserva"""
        response = self.client.post("/api/reservas/", self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["status"], self.payload["status"])
        self.assertEqual(response.data["morador"], self.morador.id)

    def test_listar_reservas(self):
        """GET /api/reservas/ deve retornar reservas (paginação DRF)"""
        ReservaEspaco.objects.create(**self.model_data)
        response = self.client.get("/api/reservas/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # checa paginação padrão DRF
        self.assertIn("count", response.data)
        self.assertIn("results", response.data)
        self.assertGreaterEqual(response.data["count"], 1)
        self.assertGreaterEqual(len(response.data["results"]), 1)

    def test_atualizar_reserva(self):
        """PUT /api/reservas/{id}/ deve atualizar o status"""
        reserva = ReservaEspaco.objects.create(**self.model_data)
        novos = self.payload.copy()
        novos["status"] = "aprovado"
        response = self.client.put(f"/api/reservas/{reserva.id}/", novos, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "aprovado")

    def test_deletar_reserva(self):
        """DELETE /api/reservas/{id}/ deve remover a reserva"""
        reserva = ReservaEspaco.objects.create(**self.model_data)
        response = self.client.delete(f"/api/reservas/{reserva.id}/", format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(ReservaEspaco.objects.filter(id=reserva.id).exists())

    def test_filtrar_reservas_por_data(self):
        """GET /api/reservas/?data=... deve filtrar pela data"""
        ReservaEspaco.objects.create(**self.model_data)
        response = self.client.get(f"/api/reservas/?data={self.payload['data']}", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # todos os itens retornados devem ter a data solicitada
        for item in response.data["results"]:
            self.assertEqual(item["data"], self.payload["data"])
