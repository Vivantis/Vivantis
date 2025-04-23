from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from condominios.condominio.models import Condominio, Unidade
from condominios.moradores.models import Morador
from .models import Prestador

class PrestadorTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='vitor', password='123456', email='vitor@teste.com')
        self.condominio = Condominio.objects.create(nome="Condomínio Top", endereco="Rua Teste")
        self.unidade = Unidade.objects.create(numero="101", condominio=self.condominio)
        self.morador = Morador.objects.create(user=self.user, nome='Vitor', email='vitor@teste.com', unidade=self.unidade)
        self.prestador = Prestador.objects.create(nome="Zelador Zé", tipo_servico="Limpeza", condominio=self.condominio)
        self.client.login(username='vitor', password='123456')

    def test_listar_prestadores(self):
        response = self.client.get('/api/prestadores/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_criar_prestador(self):
        payload = {
            "nome": "Eletricista João",
            "tipo_servico": "Elétrica",
            "condominio": self.condominio.id,
        }
        response = self.client.post('/api/prestadores/', payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_editar_prestador(self):
        response = self.client.patch(f'/api/prestadores/{self.prestador.id}/', {'ativo': False})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
