from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Condominio, Documento, AdministradorGeral


class DocumentoAPITests(APITestCase):
    """
    Testes automatizados para a API de Documentos do Condomínio
    """

    def setUp(self):
        # Cria e autentica um usuário
        self.user = User.objects.create_user(username='sindico', password='admin123')
        self.client.force_authenticate(user=self.user)

        # Torna o usuário um administrador geral
        self.admin = AdministradorGeral.objects.create(user=self.user, nome='Síndico', telefone='(11) 90000-0000')

        # Cria um condomínio base
        self.condominio = Condominio.objects.create(
            nome="Residencial Aurora",
            endereco="Rua das Luzes, 101"
        )

        # Arquivo de teste simulado
        self.arquivo_teste = SimpleUploadedFile(
            "regulamento.pdf", b"Fake PDF content", content_type="application/pdf"
        )

        # Dados padrão para criação via API
        self.dados = {
            "titulo": "Regulamento Interno",
            "tipo": "regulamento",
            "arquivo": self.arquivo_teste,
            "visivel_para_moradores": True,
            "condominio": self.condominio.id,
            "enviado_por": self.user.id
        }

    def test_criar_documento(self):
        """Testa a criação de um novo documento via API"""
        response = self.client.post('/api/documentos/', self.dados, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['titulo'], self.dados['titulo'])

    def test_listar_documentos(self):
        """Testa a listagem de documentos existentes"""
        Documento.objects.create(
            titulo="Ata da reunião",
            tipo="ata",
            arquivo=self.arquivo_teste,
            condominio=self.condominio,
            enviado_por=self.user
        )
        response = self.client.get('/api/documentos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_deletar_documento(self):
        """Testa a exclusão de um documento"""
        documento = Documento.objects.create(
            titulo="Boleto Abril",
            tipo="boleto",
            arquivo=self.arquivo_teste,
            condominio=self.condominio,
            enviado_por=self.user
        )
        response = self.client.delete(f'/api/documentos/{documento.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
