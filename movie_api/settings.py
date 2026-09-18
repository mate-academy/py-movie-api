"""Settings for the Movie API project."""
from __future__ import annotations
from pathlib import Path

BASE_DIR: Path = Path(__file__).resolve().parent.parent
SECRET_KEY: str = "django-insecure-change-this-key-in-production"
DEBUG: bool = True
ALLOWED_HOSTS: list[str] = []
INSTALLED_APPS: list[str] = [
    "django.contrib.admin", "django.contrib.auth", "django.contrib.contenttypes",
    "django.contrib.sessions", "django.contrib.messages", "django.contrib.staticfiles",
    "rest_framework", "cinema",
]
MIDDLEWARE: list[str] = [
    "django.middleware.security.SecurityMiddleware", "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware", "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware", "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
ROOT_URLCONF: str = "movie_api.urls"
TEMPLATES: list[dict[str, object]] = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates", "DIRS": [], "APP_DIRS": True,
    "OPTIONS": {"context_processors": [
        "django.template.context_processors.request", "django.contrib.auth.context_processors.auth",
        "django.contrib.messages.context_processors.messages",
    ]},
}]
WSGI_APPLICATION: str = "movie_api.wsgi.application"
ASGI_APPLICATION: str = "movie_api.asgi.application"
DATABASES: dict[str, dict[str, str]] = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": str(BASE_DIR / "db.sqlite3")}
}
AUTH_PASSWORD_VALIDATORS: list[dict[str, str]] = []
LANGUAGE_CODE: str = "en-us"
TIME_ZONE: str = "UTC"
USE_I18N: bool = True
USE_TZ: bool = True
STATIC_URL: str = "static/"
DEFAULT_AUTO_FIELD: str = "django.db.models.BigAutoField"
