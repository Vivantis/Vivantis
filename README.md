# 🏢 Vivantis – Sistema de Gestão de Condomínio com IA

Sistema inteligente e modular para gestão de condomínios, desenvolvido com Django, PostgreSQL, JWT e Swagger. Permite automação de processos, registro de dados, segurança de acesso e experiências futuras com inteligência artificial.

---

## ✨ Funcionalidades atuais

- Cadastro de condomínios e suas unidades  
- Registro de moradores com vínculo à unidade  
- Gestão de prestadores de serviço  
- Registro de visitantes e controle de entrada  
- Controle de acesso (entrada e saída)  
- Ocorrências (problemas, solicitações)  
- Correspondências (entregas e retiradas)  
- Espaços comuns e reservas por moradores  
- Compartilhamento de documentos (regulamentos, boletos, atas)  
- Autenticação JWT protegendo toda a API  
- Documentação Swagger interativa  
- Testes automatizados por módulo  
- Agenda de Manutenções  
- Avisos e Comunicados  
- Administração Geral de Condomínios
- Relatórios Gerais

---

## 🧠 IA e recursos futuros

- Classificação inteligente de ocorrências por urgência  
- Geração de relatórios e dashboards  
- Análise de ocupação de espaços  
- Previsão de fluxo de visitantes  
- Alertas proativos para gestão  

---

## 🛠 Tecnologias utilizadas

- Python 3.13  
- Django 5.x  
- Django REST Framework  
- PostgreSQL  
- SimpleJWT (autenticação)  
- drf-spectacular (Swagger)  
- Git e GitHub  

---

## 🚀 Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/Vivantis.git
cd Vivantis
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados PostgreSQL

No `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'vivantis_db',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Migre e crie um superusuário

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 6. Rode o servidor

```bash
python manage.py runserver
```

---

## 🔐 Autenticação com JWT

- Obter token:
  ```http
  POST /api/token/
  ```
- Renovar token:
  ```http
  POST /api/token/refresh/
  ```
- Header:
  ```
  Authorization: Bearer <seu_token>
  ```

---

## 📑 Documentação da API

- Swagger: `http://localhost:8000/api/docs/`
- Redoc: `http://localhost:8000/api/redoc/`

---

## ✅ Módulos implementados

- ✅ Condomínio  
- ✅ Unidade  
- ✅ Morador  
- ✅ Prestador  
- ✅ Ocorrência  
- ✅ Visitante  
- ✅ Controle de Acesso  
- ✅ Correspondência  
- ✅ Espaço Comum  
- ✅ Reserva de Espaços  
- ✅ Documentos  
- ✅ Administrador Geral  
- ✅ Avisos e Comunicados  
- ✅ Agenda de Manutenções
- ✅ Relatórios Gerais
  


---

## 🧪 Testes automatizados

Executar todos os testes:

```bash
python manage.py test
```

Testes cobrem:
- CRUD de todos os módulos principais
- Respostas e status da API
- Upload de arquivos
- Criação e autenticação de usuário

---

## 👨‍💻 Autor

Projeto desenvolvido por **Vitor Alves**, **Lucas Leal** e **Caio Ferreira**  
Visão de inovação, automação e experiência condominial com IA ⚙️

---

