from pathlib import Path
import os

# ========================
# BASE
# ========================
BASE_DIR = Path(__file__).resolve().parent.parent

# ========================
# SECURITY
# ========================
SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "django-insecure-dev-key"
)

DEBUG = False


ALLOWED_HOSTS = ["*"]  # ajustar em produção

# ========================
# APPLICATIONS
# ========================
INSTALLED_APPS = [
    "jazzmin",

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    'anexos',


    "clientes",
    "calibracao",
    "comercial",
    "financeiro",
]

# ========================
# MIDDLEWARE
# ========================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

]

ROOT_URLCONF = "core.urls"

# ========================
# TEMPLATES
# ========================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

# ========================
# DATABASE
# ========================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ========================
# PASSWORD VALIDATION
# ========================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ========================
# INTERNATIONALIZATION
# ========================
LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True
USE_TZ = True

# ========================
# STATIC FILES
# ========================
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ========================
# MEDIA FILES
# ========================
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ========================
# DJANGO DEFAULTS
# ========================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_REDIRECT_URL = "/admin/"
LOGOUT_REDIRECT_URL = "/admin/login/"

# ========================
# JAZZMIN SETTINGS (LIMPO E ESTÁVEL)
# ========================

JAZZMIN_SETTINGS = {
    "site_title": "AXION",
    "site_header": "AXION",
    "site_brand": "AXION",

    "welcome_sign": "AXION — Gestão Estratégica",
    "copyright": "AXION",

    # Logos
    "site_logo": "img/logo_ds.png",
    "login_logo": "img/capa_ds.png",
    "site_logo_classes": "img-circle elevation-3",

    # UI
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,
    "navigation_expanded": True,

    # Busca global simples
    "search_model": [
        "clientes.Cliente",
    ],

    # Ícones (somente visual, sem menu customizado)
    "icons": {
        "clientes.Cliente": "fas fa-users",
        "clientes.ContatoCliente": "fas fa-id-card",

        "calibracao.Instrumento": "fas fa-tools",
        "calibracao.Calibracao": "fas fa-balance-scale",
        "calibracao.Padrao": "fas fa-ruler-combined",
        "calibracao.Documento": "fas fa-file-alt",
        "calibracao.OrdemServico": "fas fa-clipboard-list",

        "comercial.Proposta": "fas fa-file-signature",

        "financeiro.ContaReceber": "fas fa-hand-holding-usd",
        "financeiro.ContaPagar": "fas fa-file-invoice-dollar",
        "financeiro.Imposto": "fas fa-percentage",
    },
}


# ========================
# JAZZMIN UI TWEAKS
# ========================
JAZZMIN_UI_TWEAKS = {
    "brand_colour": "navbar-navy",
    "accent": "accent-primary",

    "navbar": "navbar-white navbar-light",
    "navbar_fixed": True,

    "sidebar": "sidebar-dark-navy",
    "sidebar_fixed": True,

    # 🔥 AQUI ESTÁ A CHAVE
    "sidebar_mini": True,          # menu vira “caixa”
    "sidebar_collapse": True,      # começa recolhido
    "sidebar_nav_flat_style": True,
    "sidebar_nav_legacy_style": False,

    "theme": "default",
}


