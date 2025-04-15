from pathlib import Path

# ───────────────────────────────
# 📁 Diretórios
# ───────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent

# ───────────────────────────────
# 🔐 Segurança e Debug
# ───────────────────────────────
SECRET_KEY = 'django-insecure-@2kooq@391@xs-twgg*fb-#hnflnl2^7)bwi-h=)%-am*k*wcn'
DEBUG = True  # ❗ Em produção, altere para False

ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # ❗Obrigatório se DEBUG=False

# ───────────────────────────────
# 📦 Aplicativos instalados
# ───────────────────────────────
INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'condominios',
    'rest_framework',
    'drf_spectacular',
    'drf_spectacular_sidecar',
]

# ───────────────────────────────
# ⚙️ Middlewares
# ───────────────────────────────
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ───────────────────────────────
# 🔀 URLs e WSGI
# ───────────────────────────────
ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'

# ───────────────────────────────
# 🧩 Templates
# ───────────────────────────────
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ───────────────────────────────
# 🗄 Banco de dados (PostgreSQL)
# ───────────────────────────────
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'vivantis_db',
        'USER': 'postgres',
        'PASSWORD': 'craig133',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# ───────────────────────────────
# 🔐 Validação de senha
# ───────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# ───────────────────────────────
# 🌐 Internacionalização
# ───────────────────────────────
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# ───────────────────────────────
# 📁 Arquivos estáticos
# ───────────────────────────────
STATIC_URL = 'static/'

# ───────────────────────────────
# 🔑 Campo de ID padrão
# ───────────────────────────────
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ───────────────────────────────
# 🔧 Django REST Framework
# ───────────────────────────────
REST_FRAMEWORK = {
    # Autenticação via JWT
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),

    # Permissões padrão
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    # Esquema para Swagger via drf-spectacular
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',

    # Paginação global
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,

    # Filtros globais (search, ordering, filtros customizados)
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
        'rest_framework.filters.SearchFilter',
    ],
}

# ───────────────────────────────
# 📘 Config do Swagger (drf-spectacular)
# ───────────────────────────────
SPECTACULAR_SETTINGS = {
    'TITLE': 'Vivantis API',
    'DESCRIPTION': 'Documentação interativa da API do sistema de gestão de condomínio com autenticação JWT.',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'COMPONENT_SPLIT_REQUEST': True,
}

# ───────────────────────────────
# 🌐 CORS (liberação pro front local)
# ───────────────────────────────
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5173",
]

CORS_ALLOW_CREDENTIALS = True
