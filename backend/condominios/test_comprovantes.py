from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone
from condominios.models import Condominio, Unidade, Morador, Cobranca, ComprovantePagamento


class ComprovantePagamentoAPITests(APITestCase):
    """
    Testes automatizados para o endpoint de comprovantes de pagamento.
    """

    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='admin123')
        self.client.force_authenticate(user=self.user)

        self.condominio = Condominio.objects.create(nome="Residencial Teste", endereco="Rua A, 123")
        self.unidade = Unidade.objects.create(numero="101", bloco="A", condominio=self.condominio)
        self.morador = Morador.objects.create(nome="João", email="joao@email.com", unidade=self.unidade)

        self.cobranca = Cobranca.objects.create(
            unidade=self.unidade,
            morador=self.morador,
            tipo="mensalidade",
            descricao="Maio",
            valor="300.00",
            vencimento=timezone.now().date(),
            status="pendente"
        )

        self.arquivo = SimpleUploadedFile("comprovante.pdf", b"fake-pdf-content", content_type="application/pdf")

        self.dados = {
            "cobranca": self.cobranca.id,
            "morador": self.morador.id,
            "arquivo": self.arquivo,
            "comentario": "Pagamento efetuado",
            "validado": False
        }

    def test_criar_comprovante(self):
        response = self.client.post('/api/comprovantes/', self.dados, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['comentario'], self.dados['comentario'])

    def test_listar_comprovantes(self):
        ComprovantePagamento.objects.create(
            cobranca=self.cobranca,
            morador=self.morador,
            arquivo=self.arquivo,
            comentario="Teste"
        )
        response = self.client.get('/api/comprovantes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(response.data["count"], 1)

    def test_atualizar_comprovante(self):
        comprovante = ComprovantePagamento.objects.create(
            cobranca=self.cobranca,
            morador=self.morador,
            arquivo=self.arquivo,
            comentario="Inicial"
        )

        novos_dados = {
            "comentario": "Atualizado",
            "validado": True,
            "validado_por": self.user.id
        }

        response = self.client.patch(f'/api/comprovantes/{comprovante.id}/', novos_dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['comentario'], "Atualizado")
        self.assertTrue(response.data['validado'])

    def test_deletar_comprovante(self):
        comprovante = ComprovantePagamento.objects.create(
            cobranca=self.cobranca,
            morador=self.morador,
            arquivo=self.arquivo,
            comentario="Remover"
        )
        response = self.client.delete(f'/api/comprovantes/{comprovante.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(ComprovantePagamento.objects.filter(id=comprovante.id).exists())

    def test_filtrar_por_morador(self):
        outro = Morador.objects.create(nome="Maria", email="maria@email.com", unidade=self.unidade)
        ComprovantePagamento.objects.create(cobranca=self.cobranca, morador=outro, arquivo=self.arquivo, comentario="Outro")
        ComprovantePagamento.objects.create(cobranca=self.cobranca, morador=self.morador, arquivo=self.arquivo, comentario="Principal")
        response = self.client.get(f'/api/comprovantes/?morador={self.morador.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]['morador'], self.morador.id)

    def test_filtrar_por_cobranca(self):
        ComprovantePagamento.objects.create(cobranca=self.cobranca, morador=self.morador, arquivo=self.arquivo, comentario="Com cobrança")
        response = self.client.get(f'/api/comprovantes/?cobranca={self.cobranca.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(response.data["count"], 1)

    def test_filtrar_por_validado(self):
        ComprovantePagamento.objects.create(cobranca=self.cobranca, morador=self.morador, arquivo=self.arquivo, comentario="Validado", validado=True)
        response = self.client.get('/api/comprovantes/?validado=true')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for item in response.data["results"]:
            self.assertTrue(item['validado'])

    def test_busca_por_comentario(self):
        ComprovantePagamento.objects.create(cobranca=self.cobranca, morador=self.morador, arquivo=self.arquivo, comentario="Pix bancário")
        response = self.client.get('/api/comprovantes/?search=Pix')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(response.data["count"], 1)
        self.assertIn("Pix", response.data["results"][0]['comentario'])

    def test_ordenar_por_data_envio(self):
        ComprovantePagamento.objects.create(cobranca=self.cobranca, morador=self.morador, arquivo=self.arquivo, comentario="Mais novo")
        response = self.client.get('/api/comprovantes/?ordering=-data_envio')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(response.data["count"], 1)
