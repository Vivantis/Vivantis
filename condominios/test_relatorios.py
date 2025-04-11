from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.utils import timezone
from .models import (
    Condominio, Morador, Ocorrencia, Visitante, Unidade,
    EspacoComum, ReservaEspaco, AdministradorGeral
)


class RelatorioGeralAPITests(APITestCase):
    """
    Testes automatizados para o endpoint de relatório geral.
    """

    def setUp(self):
        # Cria e autentica usuário
        self.user = User.objects.create_user(username='admin', password='admin123')
        self.client.force_authenticate(user=self.user)

        # Torna o usuário um administrador geral
        self.admin = AdministradorGeral.objects.create(user=self.user, nome="Admin Teste", telefone="(11) 90000-0000")

        # Cria dados simulados para o relatório
        self.condominio = Condominio.objects.create(nome="Condomínio Teste", endereco="Rua Exemplo, 123")
        self.unidade = Unidade.objects.create(numero="101", bloco="A", condominio=self.condominio)
        self.morador = Morador.objects.create(nome="João", email="joao@email.com", unidade=self.unidade)

        # Cria uma ocorrência aberta
        Ocorrencia.objects.create(
            titulo="Vazamento",
            descricao="Vazamento no banheiro",
            status="aberta",
            morador=self.morador,
            unidade=self.unidade
        )

        # Cria visitante hoje
        Visitante.objects.create(
            nome="Visitante 1",
            documento="123456789",
            unidade=self.unidade,
            morador_responsavel=self.morador
        )

        # Cria espaço comum e reserva
        espaco = EspacoComum.objects.create(nome="Salão de Festas", condominio=self.condominio)
        ReservaEspaco.objects.create(
            espaco=espaco,
            morador=self.morador,
            unidade=self.unidade,
            data_reserva=timezone.now().date(),
            horario_inicio="18:00",
            horario_fim="22:00",
            status="aprovado"
        )

    def test_relatorio_geral_retorna_dados(self):
        """
        Testa se o endpoint de relatório geral retorna dados e status 200.
        """
        response = self.client.get('/api/relatorios/geral/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('total_condominios', response.data)
        self.assertIn('total_moradores', response.data)
        self.assertIn('total_ocorrencias_abertas', response.data)
        self.assertIn('total_visitantes_hoje', response.data)
        self.assertIn('reservas_por_espaco', response.data)
