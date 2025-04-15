from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from datetime import date, timedelta
from condominios.models import (
    Condominio, Unidade, Morador,
    EspacoComum, ReservaEspaco, AdministradorGeral
)


class ReservaEspacoAPITests(APITestCase):
    """
    Testes automatizados para a API de Reservas de Espaços
    """

    def setUp(self):
        # Cria o usuário e autentica como administrador geral
        self.user = User.objects.create_user(username='moradora', email='julia@example.com', password='admin123')
        self.admin = AdministradorGeral.objects.create(user=self.user, nome='Admin Teste', telefone='11999999999')
        self.client.force_authenticate(user=self.user)

        # Dados de base para o teste
        self.condominio = Condominio.objects.create(nome="Residencial Morada", endereco="Rua 10, nº 50")
        self.unidade = Unidade.objects.create(numero="101", bloco="A", condominio=self.condominio)
        self.morador = Morador.objects.create(nome="Julia Moradora", email="julia@example.com", unidade=self.unidade)
        self.espaco = EspacoComum.objects.create(nome="Salão de Festas", condominio=self.condominio)

        # Data futura para garantir validade nos testes
        self.data_futura = (date.today() + timedelta(days=30)).isoformat()

        # Dados padrão para criação via API
        self.dados = {
            "morador": self.morador.id,
            "unidade": self.unidade.id,
            "espaco": self.espaco.id,
            "data": self.data_futura,
            "horario_inicio": "18:00",
            "horario_fim": "22:00",
            "status": "pendente",
            "observacoes": "Aniversário de criança"
        }

    def test_criar_reserva(self):
        """Testa a criação de uma nova reserva"""
        response = self.client.post('/api/reservas/', self.dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('status'), "pendente")
        self.assertEqual(response.data.get('morador'), self.morador.id)
        self.assertEqual(response.data.get('unidade'), self.unidade.id)

    def test_listar_reservas(self):
        """Testa a listagem de reservas"""
        ReservaEspaco.objects.create(
            morador=self.morador,
            unidade=self.unidade,
            espaco=self.espaco,
            data=self.data_futura,
            horario_inicio="14:00",
            horario_fim="18:00",
            status="aprovado"
        )
        response = self.client.get('/api/reservas/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("results", response.data)
        self.assertGreaterEqual(len(response.data["results"]), 1)

    def test_atualizar_reserva(self):
        """Testa a atualização de uma reserva"""
        reserva = ReservaEspaco.objects.create(
            morador=self.morador,
            unidade=self.unidade,
            espaco=self.espaco,
            data=self.data_futura,
            horario_inicio="10:00",
            horario_fim="12:00",
            status="pendente"
        )
        novos_dados = {
            "morador": self.morador.id,
            "unidade": self.unidade.id,
            "espaco": self.espaco.id,
            "data": self.data_futura,
            "horario_inicio": "10:00",
            "horario_fim": "12:00",
            "status": "aprovado",
            "observacoes": "Confirmada pela administração"
        }
        response = self.client.put(f'/api/reservas/{reserva.id}/', novos_dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('status'), "aprovado")
        self.assertEqual(response.data.get('observacoes'), "Confirmada pela administração")

    def test_deletar_reserva(self):
        """Testa a exclusão de uma reserva"""
        reserva = ReservaEspaco.objects.create(
            morador=self.morador,
            unidade=self.unidade,
            espaco=self.espaco,
            data=self.data_futura,
            horario_inicio="16:00",
            horario_fim="20:00",
            status="pendente"
        )
        response = self.client.delete(f'/api/reservas/{reserva.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(ReservaEspaco.objects.filter(id=reserva.id).exists())
