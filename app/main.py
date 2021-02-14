from functools import lru_cache

from fastapi import Depends, FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core import config


@lru_cache
def get_settings():
    return config.Settings()


def get_application() -> FastAPI:
    settings = get_settings()

    application = FastAPI(
        title=settings.project_name,
        version=settings.version,
        debug=settings.debug,
        description=settings.project_description,
    )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return application


app = get_application()
