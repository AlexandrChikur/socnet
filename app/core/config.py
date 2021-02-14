from functools import lru_cache

from pydantic import BaseSettings


@lru_cache
def get_settings():
    return Settings()


class Settings(BaseSettings):
    project_name: str = "SocNetAPI"
    project_description: str = ""
    version: str = "0.0.0"

    debug: bool = False
    api_prefix: str = "/api"

    database_url: str

    class Config:
        env_file = ".env"
