from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Condominio, Aviso


class AvisoAPITests(APITestCase):
    """
    Testes automatizados para a API de Avisos e Comunicados
    """

    def setUp(self):
        # Cria e autentica um usuário (síndico)
        self.user = User.objects.create_user(username='sindico', password='admin123')
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
        Aviso.objects.create(
            titulo="Manutenção na piscina",
            mensagem="A manutenção será realizada no dia 15 de março.",
            condominio=self.condominio,
            publicado_por=self.user
        )
        response = self.client.get('/api/avisos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

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
        self.assertEqual(response.data['titulo'], "Portão fechado - Atualização")

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
