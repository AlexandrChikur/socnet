from functools import lru_cache

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core import config
from app.core.events import create_shutdown_eventhandler, create_startup_eventhandler


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

    # fmt: off
    application.add_event_handler('startup', create_startup_eventhandler(application))
    application.add_event_handler('shutdown', create_shutdown_eventhandler(application))
    # fmt: on

    return application


app = get_application()
