import os
from dotenv import load_dotenv

load_dotenv(os.path.join(".env"))

SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = os.environ.get("DEBUG")
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(",")

# Postgres db informations
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

DOMAIN = os.environ.get("DOMAIN")

# Payme
PAYME_KEY = os.environ.get("PAYME_KEY")
PAYME_TEST_KEY = os.environ.get("PAYME_TEST_KEY")

# App API url
API_URL = os.environ.get("API_URL")