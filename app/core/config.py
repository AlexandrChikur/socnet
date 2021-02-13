from pydantic import BaseSettings


class Settings(BaseSettings):
    project_name: str = "SocNetAPI"
    project_description: str = ""
    version: str = "0.0.0"
    debug: bool = False
    api_prefix: str = "/api"

    class Config:
        env_file = ".env"
