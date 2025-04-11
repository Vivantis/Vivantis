from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Condominio, Unidade, Morador, Cobranca, AdministradorGeral


class CobrancaAPITests(APITestCase):
    """
    Testes automatizados para o endpoint de cobranças financeiras.
    """

    def setUp(self):
        # Cria usuário com perfil de AdministradorGeral
        self.user = User.objects.create_user(username='admin', password='admin123')
        self.admin_profile = AdministradorGeral.objects.create(user=self.user, nome='Admin Teste', telefone='(11) 91111-2222')
        self.client.force_authenticate(user=self.user)

        # Cria estrutura de dados base
        self.condominio = Condominio.objects.create(nome="Residencial Teste", endereco="Rua Central, 123")
        self.unidade = Unidade.objects.create(numero="101", bloco="A", condominio=self.condominio)
        self.morador = Morador.objects.create(nome="João", email="joao@email.com", unidade=self.unidade)

        # Dados de cobrança para API (com IDs)
        self.dados = {
            "unidade": self.unidade.id,
            "morador": self.morador.id,
            "tipo": "mensalidade",
            "descricao": "Taxa de Abril",
            "valor": "300.00",
            "vencimento": timezone.now().date(),
            "status": "pendente"
        }

    def test_criar_cobranca(self):
        """Testa a criação de uma cobrança via API"""
        response = self.client.post('/api/cobrancas/', self.dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['valor'], self.dados['valor'])

    def test_listar_cobrancas(self):
        """Testa a listagem de cobranças"""
        Cobranca.objects.create(
            unidade=self.unidade,
            morador=self.morador,
            tipo="mensalidade",
            descricao="Maio",
            valor="300.00",
            vencimento=timezone.now().date(),
            status="pendente"
        )
        response = self.client.get('/api/cobrancas/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_atualizar_cobranca(self):
        """Testa a atualização de uma cobrança"""
        cobranca = Cobranca.objects.create(
            unidade=self.unidade,
            morador=self.morador,
            tipo="mensalidade",
            descricao="Taxa de Abril",
            valor="300.00",
            vencimento=timezone.now().date(),
            status="pendente"
        )
        novos_dados = {
            "unidade": self.unidade.id,
            "morador": self.morador.id,
            "tipo": "mensalidade",
            "descricao": "Atualizado",
            "valor": "350.00",
            "vencimento": timezone.now().date(),
            "status": "pago"
        }
        response = self.client.put(f'/api/cobrancas/{cobranca.id}/', novos_dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], "pago")

    def test_deletar_cobranca(self):
        """Testa a exclusão de uma cobrança"""
        cobranca = Cobranca.objects.create(
            unidade=self.unidade,
            morador=self.morador,
            tipo="mensalidade",
            descricao="Taxa de Abril",
            valor="300.00",
            vencimento=timezone.now().date(),
            status="pendente"
        )
        response = self.client.delete(f'/api/cobrancas/{cobranca.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Cobranca.objects.filter(id=cobranca.id).exists())
