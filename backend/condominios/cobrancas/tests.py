from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.utils import timezone
from condominios.models import Condominio, Unidade, Morador, Cobranca, AdministradorGeral


class CobrancaAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='admin123')
        self.admin = AdministradorGeral.objects.create(user=self.user, nome="Administrador", telefone="(11) 99999-9999")
        self.client.force_authenticate(user=self.user)

        self.condominio = Condominio.objects.create(nome="Condomínio Sol", endereco="Rua Teste, 123")
        self.unidade = Unidade.objects.create(numero="101", bloco="A", condominio=self.condominio)
        self.morador = Morador.objects.create(nome="Carlos", email="carlos@email.com", unidade=self.unidade)

        # Para requisições via API (com IDs)
        self.payload = {
            "unidade": self.unidade.id,
            "morador": self.morador.id,
            "tipo": "mensalidade",
            "descricao": "Cobrança de Abril",
            "valor": "300.00",
            "vencimento": timezone.now().date(),
            "status": "pendente"
        }

        # Para uso direto com Cobranca.objects.create()
        self.model_data = {
            "unidade": self.unidade,
            "morador": self.morador,
            "tipo": "mensalidade",
            "descricao": "Cobrança de Abril",
            "valor": "300.00",
            "vencimento": timezone.now().date(),
            "status": "pendente"
        }

    def test_criar_cobranca(self):
        response = self.client.post('/api/cobrancas/', self.payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_listar_cobrancas(self):
        Cobranca.objects.create(**self.model_data)
        response = self.client.get('/api/cobrancas/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(response.data["count"], 1)

    def test_atualizar_cobranca(self):
        cobranca = Cobranca.objects.create(**self.model_data)
        novos_dados = self.payload.copy()
        novos_dados.update({"descricao": "Atualizado", "status": "pago"})
        response = self.client.put(f'/api/cobrancas/{cobranca.id}/', novos_dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "pago")

    def test_deletar_cobranca(self):
        cobranca = Cobranca.objects.create(**self.model_data)
        response = self.client.delete(f'/api/cobrancas/{cobranca.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Cobranca.objects.filter(id=cobranca.id).exists())

    def test_filtrar_por_status(self):
        Cobranca.objects.create(**self.model_data)
        response = self.client.get('/api/cobrancas/?status=pendente')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data["results"]), 1)

    def test_filtrar_por_morador(self):
        Cobranca.objects.create(**self.model_data)
        response = self.client.get(f'/api/cobrancas/?morador={self.morador.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for cobranca in response.data["results"]:
            self.assertEqual(cobranca["morador"], self.morador.id)

    def test_filtrar_por_tipo(self):
        Cobranca.objects.create(**self.model_data)
        response = self.client.get('/api/cobrancas/?tipo=mensalidade')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for cobranca in response.data["results"]:
            self.assertEqual(cobranca["tipo"], "mensalidade")
