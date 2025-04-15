# 🏢 Vivantis – Sistema de Gestão de Condomínio com IA

Sistema modular, robusto e inteligente desenvolvido com Django + PostgreSQL para facilitar a gestão de condomínios residenciais. O Vivantis une **tecnologia, automação e segurança** em uma só plataforma, com visão futura de integração com inteligência artificial.

---

## 🚀 Funcionalidades principais

✅ Cadastro e gerenciamento de **condomínios** e **unidades**  
👤 Registro de **moradores**, com vínculo à unidade  
💼 Gestão de **prestadores de serviço**  
📮 Controle de **correspondências recebidas e retiradas**  
📎 Upload e gerenciamento de **documentos internos** (regulamentos, atas, boletos)  
📅 **Reservas de espaços comuns** com controle de status e agenda  
🔐 **Controle de acesso** de moradores, visitantes e prestadores  
🛠️ Gestão de **manutenções planejadas** e ocorrências  
📢 Publicação de **avisos e comunicados** para o condomínio  
🧾 **Comprovantes de pagamento** vinculados a cobranças  
👮 Aprovação de usuários com autenticação via **JWT Token**  
🧠 Pronto para integração com **IA** (dashboards, alertas, previsões futuras)

---

## 🔍 Funcionalidades recentes

🆕 **Filtragem inteligente nas APIs de:**

### ✅ Comprovantes de Pagamento
- Por morador  
- Por cobrança  
- Por status de validação  

### ✅ Moradores
- Por nome  
- Por e-mail  
- Por unidade  

### ✅ Visitantes
- Por nome  
- Por documento  

### ✅ Ocorrências
- Por status  
- Por título  
- Por unidade  

### ✅ Documentos
- Por título  
- Por tipo  

### ✅ Prestadores de Serviço
- Por nome  

### ✅ Cadastro e Aprovação de Usuários
- Cadastro com ativação via painel do administrador  
- Endpoint protegido para aprovação manual  

✨ Todas as funcionalidades contam com testes automatizados, garantindo estabilidade para produção e integração com o front-end.

---

## 🛠️ Tecnologias utilizadas

**Backend:**
- Python 3.13  
- Django 5.x  
- Django REST Framework  
- PostgreSQL  
- JWT (SimpleJWT)  
- Swagger (drf-spectacular)  
- Redoc  
- Pytest / Django TestCase  

**Frontend:**
- Next.js 14 (App Router + TypeScript)  
- TailwindCSS  
- Tema Claro/Escuro  
- Arquitetura Mobile-First  
- Suporte a PWA (em desenvolvimento) 

## 🚀 Como rodar o projeto localmente (Backend)

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

# 🚀 Como rodar o projeto localmente (Frontend)

### 1. Rodando o Frontend (Next.js)

```bash
Copiar
cd frontend
npm install
npm run dev
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

🧠 Visão futura com IA

🔎 Classificação automática de ocorrências

📊 Dashboards inteligentes com indicadores por condomínio

🔔 Alertas preditivos (manutenções, visitantes, vencimentos)

🤖 Integração com chatbots para autoatendimento

## 👨‍💻 Autor

Projeto desenvolvido por **Vitor Alves**, **Lucas Leal** e **Caio Ferreira**  
Visão de inovação, automação e experiência condominial com IA ⚙️
