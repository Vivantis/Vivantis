# 🏢 Vivantis – Sistema de Gestão de Condomínio com IA

Sistema inteligente para gestão de condomínios com foco em automação, eficiência e comunicação clara entre síndicos, moradores e prestadores de serviço. Desenvolvido com **Django**, **PostgreSQL**, **JWT** e arquitetura modular via API REST.

---

## ✨ Funcionalidades atuais

- Cadastro e gestão de condomínios
- Cadastro de unidades e vínculo com moradores
- Registro de moradores e suas unidades
- Autenticação com JWT
- Cadastro de prestadores de serviço
- Documentação interativa da API via Swagger
- Testes automatizados com cobertura básica
- Banco de dados PostgreSQL
- Proteção por autenticação e permissões (token obrigatório)

---

## 🧠 Inteligência Artificial (em construção futura)

- Processamento inteligente de ocorrências
- Geração de relatórios de gestão com insights
- IA para priorização de demandas e previsões administrativas
- Automatização de comunicação com moradores

---

## 🛠 Tecnologias utilizadas

- Python 3.13
- Django 5.x
- Django REST Framework
- PostgreSQL
- SimpleJWT (autenticação)
- drf-spectacular (Swagger UI)
- Git e GitHub

---

## 🚀 Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/viithalves/Vivantis.git
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

### 4. Configure o banco de dados PostgreSQL em `settings.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nome_do_banco',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Rode as migrações e crie um superusuário

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 6. Rode o servidor local

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
- Use nos headers:
  ```
  Authorization: Bearer <seu_token>
  ```

---

## 📑 Documentação da API

- Swagger: `http://localhost:8000/api/docs/`
- Redoc: `http://localhost:8000/api/redoc/`

---

## ✅ Módulos implementados até agora

| Módulo       | Status | Funcionalidade                             |
|--------------|--------|--------------------------------------------|
| Condomínio   | ✅     | Cadastro e listagem de condomínios         |
| Unidade      | ✅     | Cadastro e vínculo com condomínio          |
| Morador      | ✅     | Cadastro e vínculo com unidade             |
| Ocorrência   | 🔄     | Em andamento                               |
| Prestadores  | ✅     | Cadastro e vínculo com condomínio          |

---

## 🧪 Testes

Executar:

```bash
python manage.py test
```

Testes incluídos para:
- Condomínios
- Unidades
- Moradores
- Prestadores

---

## 🤝 Contribuição e Time

Este projeto é construído por uma equipe com visão estratégica e foco em inovação para soluções condominiais.  
Contribuições são bem-vindas!  
Autor atual: **Vitor Alves**

---

