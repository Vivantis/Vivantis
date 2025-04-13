from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Prestador, Condominio

class PrestadorAPITests(APITestCase):
    """
    Testes automatizados para a API de Prestadores.
    """

    def setUp(self):
        # Cria e autentica um usuário
        self.user = User.objects.create_user(username='admin', password='admin123')
        self.client.force_authenticate(user=self.user)

        # Cria um condomínio para associar aos prestadores
        self.condominio = Condominio.objects.create(
            nome='Residencial Teste',
            endereco='Rua Teste, 123'
        )

        # Dados para envio via API (aqui sim usamos o ID)
        self.dados = {
            "nome": "João Prestador",
            "tipo_servico": "Jardinagem",
            "telefone": "(11) 99999-8888",
            "condominio": self.condominio.id  # OK porque é via JSON/API
        }

    def test_criar_prestador(self):
        """Testa a criação de um novo prestador via API"""
        response = self.client.post('/api/prestadores/', self.dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nome'], self.dados['nome'])

    def test_listar_prestadores(self):
        """Testa a listagem de prestadores"""
        # Aqui usamos a instância do condomínio (não o ID)
        Prestador.objects.create(
            nome="Maria Serviços",
            tipo_servico="Limpeza",
            telefone="(11) 98888-7777",
            condominio=self.condominio
        )
        response = self.client.get('/api/prestadores/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_atualizar_prestador(self):
        """Testa a atualização dos dados de um prestador"""
        prestador = Prestador.objects.create(
            nome="Carlos Eletricista",
            tipo_servico="Elétrica",
            telefone="(11) 97777-6666",
            condominio=self.condominio
        )
        novos_dados = {
            "nome": "Carlos Atualizado",
            "tipo_servico": "Elétrica",
            "telefone": "(11) 97777-0000",
            "condominio": self.condominio.id
        }
        response = self.client.put(f'/api/prestadores/{prestador.id}/', novos_dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], "Carlos Atualizado")

    def test_deletar_prestador(self):
        """Testa a exclusão de um prestador"""
        prestador = Prestador.objects.create(
            nome="Marcelo Seguranças",
            tipo_servico="Portaria",
            telefone="(11) 95555-4444",
            condominio=self.condominio
        )
        response = self.client.delete(f'/api/prestadores/{prestador.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Prestador.objects.filter(id=prestador.id).exists())
