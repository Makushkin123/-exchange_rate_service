from app.service.exchange_rate_service import ExchangeRateService

from app.models.dp_helper import db_helper
from app.di.di import get_database_repository, get_source_currency_factory
from app.config import settings
import asyncio


async def set_actual_currency_rate_to_db():
    repository = get_database_repository()
    source_currency_factory = get_source_currency_factory()
    async with db_helper.session_factory() as session:
        exchange_rate_service = ExchangeRateService(
            session=session,
            repository=repository,
            source_currency_factory=source_currency_factory,
        )
    await exchange_rate_service.set_exchange_rate(
        source_url=settings.source_url.source_russian_bank
    )
