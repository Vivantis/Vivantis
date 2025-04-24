from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

from condominios.relatorios.models import Relatorio


class RelatorioAPITests(APITestCase):
    """
    Testes para o endpoint de Relatórios
    """

    def setUp(self):
        self.user = User.objects.create_user(username='vitor', password='123456')
        # Autentica via APIClient
        self.client.force_authenticate(user=self.user)

    def test_criar_relatorio(self):
        """POST /api/relatorios/ deve criar um relatório e retornar seus dados"""
        payload = {
            'titulo': 'Relatório de Teste',
            'tipo': 'Acessos',
            'observacoes': 'Gerado em teste.'
        }
        response = self.client.post('/api/relatorios/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data = response.data
        # Confirma que os campos foram gravados corretamente
        self.assertEqual(data['titulo'], payload['titulo'])
        self.assertEqual(data['tipo'], payload['tipo'])
        self.assertEqual(data['observacoes'], payload['observacoes'])
        self.assertEqual(data['gerado_por'], self.user.id)

    def test_listar_relatorios_usuario(self):
        """GET /api/relatorios/ deve retornar apenas os relatórios gerados pelo usuário"""
        # cria um relatório de teste vinculado ao self.user
        Relatorio.objects.create(
            titulo='R1', tipo='Teste', observacoes='Obs', gerado_por=self.user
        )

        response = self.client.get('/api/relatorios/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # verifica paginação DRF: count + results
        self.assertIn('count', response.data)
        self.assertIn('results', response.data)

        self.assertEqual(response.data['count'], 1)
        self.assertEqual(len(response.data['results']), 1)

        # valida que o relatório retornado pertence ao usuário
        rel = response.data['results'][0]
        self.assertEqual(rel['gerado_por'], self.user.id)
        self.assertEqual(rel['titulo'], 'R1')
