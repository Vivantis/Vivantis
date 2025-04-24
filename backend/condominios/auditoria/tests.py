from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

from condominios.condominio.models import Condominio
from condominios.unidade.models import Unidade
from condominios.morador.models import Morador
from condominios.autorizacoes.models import AutorizacaoEntrada
from condominios.auditoria.models import Auditoria


class AuditoriaAPITests(APITestCase):
    """
    Testa se as ações importantes estão sendo registradas corretamente
    no histórico de auditoria.
    """

    def setUp(self):
        # Portária cria autorização
        self.user_portaria = User.objects.create_user(username='porteiro', password='123')
        self.client.force_authenticate(user=self.user_portaria)

        # Cria Condomínio e Unidade
        self.condominio = Condominio.objects.create(nome="Condomínio Teste", endereco="Rua A, 123")
        self.unidade = Unidade.objects.create(numero="101", bloco="A", condominio=self.condominio)

        # Morador que aprova/recusa
        self.user_morador = User.objects.create_user(
            username='morador', email='morador@email.com', password='123'
        )
        self.morador = Morador.objects.create(
            nome="Morador Teste", email=self.user_morador.email, unidade=self.unidade
        )

        # Dados da autorização
        self.dados_autorizacao = {
            "nome_visitante": "Carlos Visitante",
            "documento_visitante": "123456789",
            "unidade_destino": self.unidade.id,
            "observacoes": "Vai chegar às 17h"
        }

    def test_auditoria_ao_criar_autorizacao(self):
        """Criação de autorização gera registro na Auditoria"""
        response = self.client.post('/api/autorizacoes/', self.dados_autorizacao, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        registros = Auditoria.objects.filter(entidade='AutorizacaoEntrada')
        self.assertEqual(registros.count(), 1)
        log = registros.first()
        self.assertEqual(log.tipo_acao, 'criado')
        self.assertIn("Solicitação criada", log.descricao)

    def test_auditoria_ao_responder_autorizacao(self):
        """Aprovação de autorização gera registro na Auditoria"""
        autorizacao = AutorizacaoEntrada.objects.create(
            nome_visitante="Carlos",
            documento_visitante="123",
            unidade_destino=self.unidade,
            criado_por=self.user_portaria
        )

        # Morador aprova
        self.client.force_authenticate(user=self.user_morador)
        response = self.client.patch(
            f'/api/autorizacoes/{autorizacao.id}/',
            {"status": "aprovada"},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        registros = Auditoria.objects.filter(
            entidade='AutorizacaoEntrada',
            objeto_id=autorizacao.id
        )
        self.assertEqual(registros.count(), 1)
        self.assertEqual(registros.first().tipo_acao, 'editado')
