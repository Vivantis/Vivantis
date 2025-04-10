# 🏢 Vivantis – Sistema de Gestão de Condomínio com IA

Este é um sistema inteligente para gestão de condomínios, com foco em melhorar a comunicação, organização e eficiência da administração. Desenvolvido com **Python (Django)** e **PostgreSQL**, este projeto visa automatizar tarefas e oferecer uma interface moderna e amigável para síndicos, moradores e prestadores de serviço.

---

## ✨ Funcionalidades

- Cadastro de usuários (síndicos, moradores, porteiros, etc)
- Gestão de chamados e ocorrências
- Controle de acesso e agendamentos de áreas comuns
- Registro inteligente de interações via IA
- Dashboard para administração e relatórios
- Integração com PostgreSQL
- API REST protegida com autenticação JWT
- Documentação interativa com Swagger

---

## 🧠 Inteligência Artificial

A IA será usada para:
- Interpretar pedidos dos moradores
- Sugerir ações automáticas com base no histórico
- Ajudar a administração a priorizar demandas
- Automatizar respostas e interações do sistema

---

## 🛠 Tecnologias utilizadas

- Python 3.x
- Django 5+
- Django REST Framework
- PostgreSQL
- Simple JWT (Autenticação com Token)
- drf-spectacular (Documentação Swagger)
- Git + GitHub

---

## ⚙️ Como rodar o projeto localmente

1. **Clone este repositório:**

```bash
git clone https://github.com/viithalves/Vivantis.git
cd Vivantis
```

2. **Crie um ambiente virtual:**

```bash
python -m venv venv
```

3. **Ative o ambiente virtual:**

- Windows:

```bash
.\venv\Scripts\activate
```

- Mac/Linux:

```bash
source venv/bin/activate
```

4. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

5. **Configure o banco PostgreSQL no `settings.py`**

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'seu_banco',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

6. **Execute as migrações:**

```bash
python manage.py makemigrations
python manage.py migrate
```

7. **Crie um superusuário:**

```bash
python manage.py createsuperuser
```

8. **Rode o servidor:**

```bash
python manage.py runserver
```

---

## 🔐 Autenticação com JWT

Para obter o token de acesso e autenticar:

- Endpoint: `POST /api/token/`
- Enviar: `username` e `password`
- Recebe: `access` e `refresh` tokens
- Use o `access` em endpoints protegidos com o header:

```http
Authorization: Bearer seu_token
```

---

## 📑 Documentação Swagger

Acesse a documentação interativa em:

```
http://localhost:8000/api/docs/
```

---

## 🤝 Colaboração

Caso queira contribuir:

- Fork o repositório
- Crie uma branch: `git checkout -b sua-feature`
- Commit suas mudanças: `git commit -m 'Minha contribuição'`
- Push: `git push origin sua-feature`
- Crie um Pull Request

---

## 📄 Licença

Este projeto está sob a licença MIT.
