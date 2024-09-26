import logging
from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
)
from fastapi.responses import JSONResponse
from app.service.exchange_rate_service import ExchangeRateServiceProtocol,
from app.di.di import get_exchange_rate_service
from app.dto.dto import ValueNameDto

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/exchange_rate/{char_code}")
async def get_exchange_rate_by_char_code(
    value: ValueNameDto,
    exchange_rate_service: ExchangeRateServiceProtocol = Annotated[
        ExchangeRateServiceProtocol,
        Depends(get_exchange_rate_service)
    ],
):
    await exchange_rate_service.
    return JSONResponse(content={"status": "good"})
