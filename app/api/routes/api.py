from typing import Any, Dict

from app.core.config import Settings, get_settings
from fastapi import APIRouter, Depends

from .v1 import api as api_v1

router = APIRouter()

# fmt: off
router.include_router(api_v1.router, prefix="/v1", tags=["v1"])
# fmt: on


@router.get("/")
async def api_info(settings: Settings = Depends(get_settings)) -> Dict[str, Any]:
    """ Endpoint that give an info about API """

    return {
        "project_name": settings.project_name,
        "project_description": settings.project_description,
        "version": settings.version,
    }
