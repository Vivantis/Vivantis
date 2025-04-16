from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from condominios.models import Condominio, Unidade, Morador, EspacoComum, ReservaEspaco


class ReservaEspacoAPITests(APITestCase):
    """
    Testes automatizados para a API de Reservas de Espaços
    """

    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='admin123')
        self.client.force_authenticate(user=self.user)

        self.condominio = Condominio.objects.create(nome="Condomínio Reserva", endereco="Rua das Reservas, 789")
        self.unidade = Unidade.objects.create(numero="101", bloco="A", condominio=self.condominio)
        self.morador = Morador.objects.create(nome="Maria Reservadora", email="maria@exemplo.com", unidade=self.unidade)
        self.espaco = EspacoComum.objects.create(nome="Salão de Festas", condominio=self.condominio)

        self.dados_reserva = {
            "morador": self.morador.id,
            "unidade": self.unidade.id,
            "espaco": self.espaco.id,
            "data": "2025-04-20",
            "horario_inicio": "14:00",
            "horario_fim": "18:00",
            "status": "pendente",
            "observacoes": "Festa de aniversário"
        }

    def test_criar_reserva(self):
        response = self.client.post('/api/reservas/', self.dados_reserva, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["status"], "pendente")

    def test_listar_reservas(self):
        ReservaEspaco.objects.create(**self.dados_reserva)
        response = self.client.get('/api/reservas/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data["results"]), 1)

    def test_atualizar_reserva(self):
        reserva = ReservaEspaco.objects.create(**self.dados_reserva)
        novos_dados = self.dados_reserva.copy()
        novos_dados["status"] = "aprovado"
        response = self.client.put(f'/api/reservas/{reserva.id}/', novos_dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "aprovado")

    def test_deletar_reserva(self):
        reserva = ReservaEspaco.objects.create(**self.dados_reserva)
        response = self.client.delete(f'/api/reservas/{reserva.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_filtrar_reservas_por_data(self):
        ReservaEspaco.objects.create(**self.dados_reserva)
        response = self.client.get(f'/api/reservas/?data={self.dados_reserva["data"]}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(res["data"] == self.dados_reserva["data"] for res in response.data["results"]))
