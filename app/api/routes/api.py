from typing import Any, Dict

from fastapi import APIRouter, Depends

from app.core.config import Settings, get_settings

router = APIRouter(
    tags=[
        "v1",
    ]
)

@router.get("/")
async def api_info(settings: Settings = Depends(get_settings)) -> Dict[str, Any]:
    """ Endpoint that give an info about API """

    return {
        "project_name": settings.project_name,
        "project_description": settings.project_description,
        "version": settings.version,
    }
