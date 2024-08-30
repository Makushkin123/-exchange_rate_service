import logging

from fastapi import (
    APIRouter,
    Depends,
)
from fastapi.responses import JSONResponse

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/test")
async def test():
    return JSONResponse(content={"status": "good"})
