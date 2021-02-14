from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.routes.api import router as api_router
from app.core import config
from app.core.events import create_shutdown_eventhandler, create_startup_eventhandler


def get_application() -> FastAPI:
    application = FastAPI(
        title=config.PROJECT_NAME,
        version=config.VERSION,
        debug=config.DEBUG,
        description=config.PROJECT_DESCRIPTION,
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

    application.include_router(
        api_router, prefix=config.API_PREFIX
    )

    return application


app = get_application()