from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from condominios.condominio.models import Condominio
from condominios.administradorgeral.models import AdministradorGeral
from condominios.avisos.models import Aviso


class AvisoAPITests(APITestCase):
    """
    Testes automatizados para a API de Avisos e Comunicados
    """

    def setUp(self):
        # Cria e autentica um usuário com perfil de AdministradorGeral (síndico)
        self.user = User.objects.create_user(username='sindico', password='admin123')
        AdministradorGeral.objects.create(
            user=self.user,
            nome='Síndico',
            telefone='(11) 98888-0000'
        )
        self.client.force_authenticate(user=self.user)

        # Cria um condomínio base
        self.condominio = Condominio.objects.create(
            nome="Residencial Aurora",
            endereco="Rua das Luzes, 101"
        )

        # Dados padrão para criação de aviso
        self.dados = {
            "titulo": "Reunião de condomínio",
            "mensagem": "A reunião ocorrerá na próxima segunda-feira às 18h.",
            "condominio": self.condominio.id,
            "publicado_por": self.user.id,
            "expira_em": "2025-12-31T23:59:59Z"
        }

    def test_criar_aviso(self):
        """Testa a criação de um novo aviso via API"""
        response = self.client.post('/api/avisos/', self.dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['titulo'], self.dados['titulo'])

    def test_listar_avisos(self):
        """Testa a listagem de avisos existentes"""
        # Cria pelo menos um aviso
        Aviso.objects.create(
            titulo="Manutenção na piscina",
            mensagem="A manutenção será realizada no dia 15 de março.",
            condominio=self.condominio,
            publicado_por=self.user
        )

        response = self.client.get('/api/avisos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Suporta respostas paginadas (campo 'results') ou não
        itens = response.data.get('results', response.data)
        self.assertGreaterEqual(len(itens), 1)

    def test_editar_aviso(self):
        """Testa a atualização dos dados de um aviso"""
        aviso = Aviso.objects.create(
            titulo="Portão fechado",
            mensagem="O portão estará fechado para manutenção.",
            condominio=self.condominio,
            publicado_por=self.user
        )
        novos_dados = {
            "titulo": "Portão fechado - Atualização",
            "mensagem": "O portão estará fechado por mais 3 dias.",
            "condominio": self.condominio.id,
            "publicado_por": self.user.id
        }
        response = self.client.put(f'/api/avisos/{aviso.id}/', novos_dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['titulo'], novos_dados['titulo'])

    def test_deletar_aviso(self):
        """Testa a exclusão de um aviso"""
        aviso = Aviso.objects.create(
            titulo="Fechamento do salão de festas",
            mensagem="O salão estará fechado para reformas.",
            condominio=self.condominio,
            publicado_por=self.user
        )
        response = self.client.delete(f'/api/avisos/{aviso.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Aviso.objects.filter(id=aviso.id).exists())
