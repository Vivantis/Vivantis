from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from condominios.models import Prestador, Condominio


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
            endereco='Rua Teste, 123',
            cidade='São Paulo',
            estado='SP',
            ativo=True
        )

        self.dados = {
            "nome": "João Prestador",
            "tipo_servico": "Jardinagem",
            "telefone": "(11) 99999-8888",
            "condominio": self.condominio.id
        }

    def test_criar_prestador(self):
        """Testa a criação de um novo prestador via POST"""
        response = self.client.post('/api/prestadores/', self.dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nome'], self.dados['nome'])

    def test_listar_prestadores(self):
        """Testa a listagem de prestadores via GET"""
        Prestador.objects.create(
            nome="Maria Serviços",
            tipo_servico="Limpeza",
            telefone="(11) 98888-7777",
            condominio=self.condominio
        )
        response = self.client.get('/api/prestadores/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data["results"]), 1)

    def test_atualizar_prestador(self):
        """Testa a atualização dos dados de um prestador via PUT"""
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
        """Testa a exclusão de um prestador via DELETE"""
        prestador = Prestador.objects.create(
            nome="Marcelo Seguranças",
            tipo_servico="Portaria",
            telefone="(11) 95555-4444",
            condominio=self.condominio
        )
        response = self.client.delete(f'/api/prestadores/{prestador.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Prestador.objects.filter(id=prestador.id).exists())

    def test_filtrar_prestadores_por_condominio(self):
        """Testa o filtro por condomínio na listagem"""
        Prestador.objects.create(
            nome="Zelador SP",
            tipo_servico="Manutenção",
            telefone="(11) 91111-2222",
            condominio=self.condominio
        )
        response = self.client.get(f'/api/prestadores/?condominio={self.condominio.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(p["condominio"] == self.condominio.id for p in response.data["results"]))

    def test_buscar_prestadores_por_nome(self):
        """Testa a busca por nome parcial via ?search=""."""
        Prestador.objects.create(
            nome="Jardineiro Top",
            tipo_servico="Jardinagem",
            telefone="(11) 92222-3333",
            condominio=self.condominio
        )
        response = self.client.get('/api/prestadores/?search=Jardineiro')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Jardineiro" in p["nome"] for p in response.data["results"]))
