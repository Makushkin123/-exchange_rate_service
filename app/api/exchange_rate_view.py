import logging
from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
)

from app.service.exchange_rate_service import ExchangeRateServiceProtocol
from app.di.di import get_exchange_rate_service
from app.dto.dto import ValueNameDto, CurrencyDto

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/exchange_rate/{char_code}")
async def get_exchange_rate_by_char_code(
    char_code: str,
    exchange_rate_service: Annotated[
        ExchangeRateServiceProtocol, Depends(get_exchange_rate_service)
    ],
):
    value = ValueNameDto(char_code=char_code)
    exchange_rate: CurrencyDto = (
        await exchange_rate_service.get_exchange_rate_by_char_code(value=value)
    )
    return exchange_rate
