from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from condominios.condominio.models import Condominio
from condominios.unidade.models import Unidade
from condominios.morador.models import Morador
from condominios.visitante.models import Visitante

class VisitanteAPITests(APITestCase):
    """
    Testes automatizados para a API de Visitantes
    """

    def setUp(self):
        # Cria e autentica um usuário
        self.user = User.objects.create_user(username='admin', password='admin123')
        self.client.force_authenticate(user=self.user)

        # Cria dados relacionados
        self.condominio = Condominio.objects.create(nome="Condomínio Modelo", endereco="Rua XPTO, 1000")
        self.unidade = Unidade.objects.create(numero="A101", bloco="A", condominio=self.condominio)
        self.morador = Morador.objects.create(nome="Maria Moradora", email="maria@example.com", unidade=self.unidade)

        # Payload padrão
        self.dados = {
            "nome": "Carlos Visitante",
            "documento": "123456789",
            "unidade": self.unidade.id,
            "morador_responsavel": self.morador.id
        }

    def test_criar_visitante(self):
        response = self.client.post('/api/visitantes/', self.dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nome'], self.dados['nome'])

    def test_listar_visitantes(self):
        Visitante.objects.create(
            nome="Ana Visitante",
            documento="987654321",
            unidade=self.unidade,
            morador_responsavel=self.morador
        )
        response = self.client.get('/api/visitantes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # DRF paginates under "results"
        self.assertGreaterEqual(len(response.data['results']), 1)

    def test_atualizar_visitante(self):
        visitante = Visitante.objects.create(
            nome="João Antigo",
            documento="000111222",
            unidade=self.unidade,
            morador_responsavel=self.morador
        )
        novos = {
            "nome": "João Atualizado",
            "documento": visitante.documento,
            "unidade": self.unidade.id,
            "morador_responsavel": self.morador.id
        }
        response = self.client.put(f'/api/visitantes/{visitante.id}/', novos, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], "João Atualizado")

    def test_deletar_visitante(self):
        visitante = Visitante.objects.create(
            nome="Temporário",
            documento="999888777",
            unidade=self.unidade,
            morador_responsavel=self.morador
        )
        response = self.client.delete(f'/api/visitantes/{visitante.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Visitante.objects.filter(id=visitante.id).exists())

    def test_filtrar_visitantes(self):
        Visitante.objects.bulk_create([
            Visitante(
                nome="Carlos Visitante",
                documento="123456789",
                unidade=self.unidade,
                morador_responsavel=self.morador
            ),
            Visitante(
                nome="Ana Visitante",
                documento="987654321",
                unidade=self.unidade,
                morador_responsavel=self.morador
            ),
        ])

        # filtrar por nome
        resp = self.client.get('/api/visitantes/?nome=Carlos')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Carlos" in v["nome"] for v in resp.data['results']))

        # filtrar por documento
        resp = self.client.get('/api/visitantes/?documento=987654321')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['results'][0]['documento'], "987654321")

        # filtrar por unidade
        resp = self.client.get(f'/api/visitantes/?unidade={self.unidade.id}')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue(all(v["unidade"] == self.unidade.id for v in resp.data['results']))

        # filtrar por morador_responsavel
        resp = self.client.get(f'/api/visitantes/?morador_responsavel={self.morador.id}')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue(all(v["morador_responsavel"] == self.morador.id for v in resp.data['results']))
