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

### Backend
- Python 3.13  
- Django 5.x  
- Django REST Framework  
- PostgreSQL  
- SimpleJWT (autenticação)  
- drf-spectacular (Swagger)  
- Git e GitHub  

### Frontend
- Next.js 14 (App Router + TypeScript)  
- TailwindCSS  
- Tema Claro/Escuro  
- Arquitetura Mobile-First  
- Suporte a PWA (em desenvolvimento)  

---

## 🚀 Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/Vivantis.git
cd Vivantis
```

### ⚙️ 2. Rodando o Backend (Django)

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

#### 2.1 Configure o banco de dados PostgreSQL

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
#### 2.2 Migre e crie um superusuário
```bash
python manage.py migrate
python manage.py runserver
```

### 2.3. Configure o banco de dados PostgreSQL

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

### 5. Migre, crie um superusuário e rode o servidor

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
### 💻 3. Rodando o Frontend (Next.js)

```bash
cd frontend
npm install
npm run dev
```

A aplicação frontend estará em: http://localhost:3000/

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
- ✅ Cobranças Financeiras  
- ✅ Comprovantes de Pagamento  
- ✅ Autorizações de Entrada  
- ✅ Auditoria de Ações  
- ✅ Perfil de Usuário (dados pessoais com autenticação)  

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

## 📄 Licença

MIT © 2025 — Vivantis Tecnologia Inteligente para Condomínios
