from typing import Any, Dict

from fastapi import APIRouter

from .v1 import api as api_v1

router = APIRouter()

# fmt: off
router.include_router(api_v1.router, prefix="/v1", tags=["v1"])
# fmt: on