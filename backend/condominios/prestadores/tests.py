from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

from condominios.condominio.models import Condominio
from condominios.unidade.models import Unidade
from condominios.morador.models import Morador
from condominios.prestadores.models import Prestador


class PrestadorAPITests(APITestCase):

    def setUp(self):
        # Usuário/Admin
        self.user = User.objects.create_user(
            username='vitor', password='123456', email='vitor@teste.com'
        )
        self.client.force_authenticate(user=self.user)

        self.condominio = Condominio.objects.create(nome="Condomínio Top", endereco="Rua Teste")
        self.unidade = Unidade.objects.create(numero="101", bloco="A", condominio=self.condominio)
        self.morador = Morador.objects.create(
            nome='Vitor', email=self.user.email, unidade=self.unidade
        )
        self.prestador = Prestador.objects.create(
            nome="Zelador Zé", tipo_servico="Limpeza", condominio=self.condominio
        )

    def test_listar_prestadores(self):
        response = self.client.get('/api/prestadores/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # DRF paginated under "results"
        self.assertGreaterEqual(len(response.data['results']), 1)

    def test_criar_prestador(self):
        payload = {
            "nome": "Eletricista João",
            "tipo_servico": "Elétrica",
            "condominio": self.condominio.id,
        }
        response = self.client.post('/api/prestadores/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_editar_prestador(self):
        response = self.client.patch(
            f'/api/prestadores/{self.prestador.id}/',
            {'ativo': False},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(response.data['ativo'])
