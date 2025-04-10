# 🏢 Vivantis – Sistema de Gestão de Condomínio com IA

Este é um sistema inteligente para gestão de condomínios, com foco em melhorar a comunicação, organização e eficiência da administração. Desenvolvido com **Python (Django)** e **PostgreSQL**, este projeto visa automatizar tarefas e oferecer uma interface moderna e amigável para síndicos, moradores e prestadores de serviço.

---

## ✨ Funcionalidades

- Cadastro de condomínios, unidades e moradores
- Autenticação JWT segura para acesso à API
- Endpoints RESTful protegidos
- Documentação da API via Swagger e Redoc
- Testes automatizados para garantir integridade do sistema
- Integração com PostgreSQL
- Pronto para expansão com módulos de controle de acesso, ocorrências, agendamentos, entre outros

---

## 🧠 Inteligência Artificial

A IA será usada futuramente para:
- Interpretar pedidos dos moradores
- Sugerir ações automáticas com base no histórico
- Ajudar a administração a priorizar demandas

---

## 🛠 Tecnologias utilizadas

- Python 3.13 + Django
- Django REST Framework
- SimpleJWT (Autenticação)
- drf-spectacular (Swagger)
- PostgreSQL
- Git + GitHub

---

## 🚀 Como rodar o projeto localmente

1. **Clone este repositório:**

```bash
git clone https://github.com/viithalves/Vivantis.git
cd Vivantis
```

2. **Crie um ambiente virtual e ative:**

```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Configure o banco PostgreSQL no `settings.py`**

5. **Rode as migrações e inicie o servidor:**

```bash
python manage.py migrate
python manage.py runserver
```

6. **Acesse a documentação interativa:**

- Swagger: `http://localhost:8000/api/docs/`
- Redoc: `http://localhost:8000/api/redoc/`

---

## 🔐 Autenticação JWT

1. Obtenha seu token via:

```
POST /api/token/
```

2. Use o token no Swagger clicando em **Authorize** e digitando:

```
Bearer seu_token_aqui
```

---

## 🧪 Testes

Execute:

```bash
python manage.py test
```

---

## 📂 Organização do Projeto

```
vivantis/
│
├── core/                # Configurações gerais do Django
├── condominios/         # App de condomínios, unidades e moradores
├── staticfiles/         # Arquivos estáticos
├── templates/           # (futuramente para frontend web)
├── requirements.txt     # Pacotes e dependências do projeto
├── README.md            # Documentação do projeto
└── manage.py            # Script principal do Django
```

---

## 🤝 Equipe

Este projeto é desenvolvido por uma equipe dedicada à inovação em soluções para administração condominial:

Caio Ferreira
Lucas Leal
Vitor Alves

---

