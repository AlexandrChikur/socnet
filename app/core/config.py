from databases import DatabaseURL
from starlette.config import Config


config = Config(".env")

PROJECT_NAME: str = config("PROJECT_NAME", cast=str, default="NoName")
PROJECT_DESCRIPTION: str = config("PROJECT_DESCRIPTION", cast=str, default="NoDescription")
VERSION: str = config("VERSION", cast=str, default="0")

DEBUG: bool = config("DEBUG", cast=bool, default=False)
API_PREFIX: str = config("API_PREFIX", cast=str, default="/api")

DATABASE_URL: DatabaseURL = config("DATABASE_URL", cast=DatabaseURL, default="postgresql://postgres:postgres@db:5432/postgres")