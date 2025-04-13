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
        # Cria e autentica um usuário
        self.user = User.objects.create_user(username='admin', password='admin123')
        self.client.force_authenticate(user=self.user)

        # Cria dados relacionados
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

        # Comprovante simulado
        self.arquivo = SimpleUploadedFile("comprovante.pdf", b"fake-pdf-content", content_type="application/pdf")

        # Dados para POST
        self.dados = {
            "cobranca": self.cobranca.id,
            "morador": self.morador.id,
            "arquivo": self.arquivo,
            "comentario": "Pagamento efetuado",
            "validado": False
        }

    def test_criar_comprovante(self):
        """Testa envio de comprovante via API"""
        response = self.client.post('/api/comprovantes/', self.dados, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['comentario'], self.dados['comentario'])

    def test_listar_comprovantes(self):
        """Testa listagem de comprovantes"""
        ComprovantePagamento.objects.create(
            cobranca=self.cobranca,
            morador=self.morador,
            arquivo=self.arquivo,
            comentario="Teste"
        )
        response = self.client.get('/api/comprovantes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_atualizar_comprovante(self):
        """Testa atualização do status de um comprovante"""
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
        """Testa exclusão de comprovante"""
        comprovante = ComprovantePagamento.objects.create(
            cobranca=self.cobranca,
            morador=self.morador,
            arquivo=self.arquivo,
            comentario="Remover"
        )
        response = self.client.delete(f'/api/comprovantes/{comprovante.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(ComprovantePagamento.objects.filter(id=comprovante.id).exists())

def test_filtrar_comprovantes_por_morador(self):
    """Testa filtro de comprovantes por morador"""
    # Cria um segundo morador
    outro_morador = Morador.objects.create(nome="Maria", email="maria@email.com", unidade=self.unidade)

    # Comprovante de Maria
    ComprovantePagamento.objects.create(
        cobranca=self.cobranca,
        morador=outro_morador,
        arquivo=self.arquivo,
        comentario="Comprovante de Maria"
    )

    # Comprovante de João (self.morador)
    ComprovantePagamento.objects.create(
        cobranca=self.cobranca,
        morador=self.morador,
        arquivo=self.arquivo,
        comentario="Comprovante do João"
    )

    # Aplica o filtro por morador
    url = f'/api/comprovantes/?morador={self.morador.id}'
    response = self.client.get(url)

    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)
    self.assertEqual(response.data[0]['morador'], self.morador.id)
