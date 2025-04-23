from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Relatorio

class RelatorioTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='vitor', password='123456')
        self.client.login(username='vitor', password='123456')

    def test_criar_relatorio(self):
        payload = {
            'titulo': 'Relatório de Teste',
            'tipo': 'Acessos',
            'observacoes': 'Gerado em teste.'
        }
        response = self.client.post('/api/relatorios/', payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_listar_relatorios_usuario(self):
        Relatorio.objects.create(titulo='R1', tipo='Teste', gerado_por=self.user)
        response = self.client.get('/api/relatorios/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
