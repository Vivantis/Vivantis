from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Ocorrencia, Condominio, Unidade, Morador


class OcorrenciaAPITests(APITestCase):
    """
    Testes automatizados para o módulo de Ocorrências
    """

    def setUp(self):
        # Criação de usuário e autenticação
        self.user = User.objects.create_user(username='admin', password='admin123')
        self.client.force_authenticate(user=self.user)

        # Criação de dados básicos para relacionamento
        self.condominio = Condominio.objects.create(nome="Condomínio Exemplo", endereco="Rua A, 123")
        self.unidade = Unidade.objects.create(numero="101", condominio=self.condominio)
        self.morador = Morador.objects.create(nome="João Morador", unidade=self.unidade)

        # Dados básicos para criar uma ocorrência
        self.dados = {
            "titulo": "Portão quebrado",
            "descricao": "O portão da garagem está travado",
            "morador": self.morador.id,
            "unidade": self.unidade.id  # Adicionado aqui
        }

    def test_criar_ocorrencia(self):
        """Testa a criação de uma nova ocorrência via API"""
        response = self.client.post('/api/ocorrencias/', self.dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['titulo'], self.dados['titulo'])

    def test_listar_ocorrencias(self):
        """Testa a listagem de ocorrências"""
        Ocorrencia.objects.create(
            titulo="Barulho excessivo",
            descricao="Barulho após horário permitido",
            morador=self.morador,
            unidade=self.unidade  # Adicionado aqui
        )
        response = self.client.get('/api/ocorrencias/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_atualizar_ocorrencia(self):
        """Testa a atualização de uma ocorrência"""
        ocorrencia = Ocorrencia.objects.create(
            titulo="Vazamento",
            descricao="Vazamento no banheiro da unidade",
            morador=self.morador,
            unidade=self.unidade  # Adicionado aqui
        )
        novos_dados = {
            "titulo": "Vazamento resolvido",
            "descricao": "Problema foi consertado",
            "morador": self.morador.id,
            "unidade": self.unidade.id  # Adicionado aqui
        }
        response = self.client.put(f'/api/ocorrencias/{ocorrencia.id}/', novos_dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['titulo'], "Vazamento resolvido")

    def test_deletar_ocorrencia(self):
        """Testa a exclusão de uma ocorrência"""
        ocorrencia = Ocorrencia.objects.create(
            titulo="Portão não fecha",
            descricao="Portão do bloco B com defeito",
            morador=self.morador,
            unidade=self.unidade  # Adicionado aqui
        )
        response = self.client.delete(f'/api/ocorrencias/{ocorrencia.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Ocorrencia.objects.filter(id=ocorrencia.id).exists())
