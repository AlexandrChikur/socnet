from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.routes.api import router as api_router
from app.core.config import get_settings
from app.core.events import create_shutdown_eventhandler, create_startup_eventhandler


def get_application() -> FastAPI:
    settings = get_settings()

    application = FastAPI(
        title=settings.project_name,
        version=settings.version,
        debug=settings.debug,
        description=settings.project_description,
    )
    
    application.state.settings = settings
    
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

    application.include_router(
        api_router, prefix=settings.api_prefix + "/v" + settings.version.split(".")[0]
    )  # Prefix is /v + MAJOR part of API version

    return application


app = get_application()
