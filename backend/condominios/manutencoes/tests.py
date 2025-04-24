from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from condominios.condominio.models import Condominio
from condominios.manutencoes.models import Manutencao
from condominios.administradorgeral.models import AdministradorGeral


class ManutencaoAPITests(APITestCase):
    """
    Testes automatizados para a API de Agenda de Manutenções
    """

    def setUp(self):
        # Cria e autentica um usuário (síndico)
        self.user = User.objects.create_user(username='sindico', password='admin123')
        self.client.force_authenticate(user=self.user)

        # Torna o usuário um administrador geral (síndico)
        self.admin = AdministradorGeral.objects.create(
            user=self.user,
            nome='Síndico',
            telefone='(11) 99999-0000'
        )

        # Cria um condomínio base com todos os campos obrigatórios
        self.condominio = Condominio.objects.create(
            nome="Residencial Aurora",
            endereco="Rua das Luzes, 101",
            cidade="São Paulo",
            estado="SP",
            ativo=True
        )

        # Dados padrão para criação de manutenção
        self.dados = {
            "titulo": "Manutenção do elevador",
            "descricao": "Substituição do motor do elevador.",
            "data_inicio": "2025-04-20T10:00:00Z",
            "data_fim": "2025-04-20T12:00:00Z",
            "status": "planejada",
            "condominio": self.condominio.id,
            "criado_por": self.user.id,
        }

    def test_criar_manutencao(self):
        """Testa a criação de uma manutenção via API"""
        response = self.client.post('/api/manutencao/', self.dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['titulo'], self.dados['titulo'])

    def test_listar_manutencao(self):
        """Testa a listagem de manutenções existentes"""
        Manutencao.objects.create(
            titulo="Manutenção da piscina",
            descricao="Limpeza e reparos.",
            data_inicio="2025-04-22T09:00:00Z",
            data_fim="2025-04-22T12:00:00Z",
            status="planejada",
            condominio=self.condominio,
            criado_por=self.user
        )
        response = self.client.get('/api/manutencao/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # DRF padrão usa paginação com 'count' e 'results'
        self.assertIn('count', response.data)
        self.assertGreaterEqual(response.data['count'], 1)
        self.assertIsInstance(response.data['results'], list)

    def test_editar_manutencao(self):
        """Testa a atualização dos dados de uma manutenção"""
        m = Manutencao.objects.create(
            titulo="Reparo no portão",
            descricao="Reparo urgente no portão da garagem.",
            data_inicio="2025-04-15T08:00:00Z",
            data_fim="2025-04-15T10:00:00Z",
            status="em_andamento",
            condominio=self.condominio,
            criado_por=self.user
        )
        novos_dados = {
            "titulo": "Reparo no portão - Urgente",
            "descricao": "Reparo urgente no portão da garagem, aumento da urgência.",
            "data_inicio": "2025-04-15T08:00:00Z",
            "data_fim": "2025-04-15T12:00:00Z",
            "status": "em_andamento",
            "condominio": self.condominio.id,
            "criado_por": self.user.id,
        }
        response = self.client.put(f'/api/manutencao/{m.id}/', novos_dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['titulo'], novos_dados['titulo'])

    def test_deletar_manutencao(self):
        """Testa a exclusão de uma manutenção"""
        m = Manutencao.objects.create(
            titulo="Troca de lâmpadas",
            descricao="Troca das lâmpadas da garagem.",
            data_inicio="2025-04-17T10:00:00Z",
            data_fim="2025-04-17T12:00:00Z",
            status="planejada",
            condominio=self.condominio,
            criado_por=self.user
        )
        response = self.client.delete(f'/api/manutencao/{m.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Manutencao.objects.filter(id=m.id).exists())
