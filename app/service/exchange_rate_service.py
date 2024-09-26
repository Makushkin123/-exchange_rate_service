from typing import Protocol

from sqlalchemy.ext.asyncio import AsyncSession

from app.managers.source_currency_manager import (
    SourceCurrencyFactory,
    SourceCurrencyManagerProtocol,
)
from app.repository.repository import RepositoryProtocol
from app.dto.dto import CurrencyDto


class ExchangeRateServiceProtocol(Protocol):
    session: AsyncSession
    repository: RepositoryProtocol
    source_currency_factory: SourceCurrencyFactory

    async def set_exchange_rate(self, source_url: str) -> None: ...


class ExchangeRateService:
    def __init__(
        self,
        session: AsyncSession,
        repository: RepositoryProtocol,
        source_currency_factory: SourceCurrencyFactory,
    ):
        self.session = session
        self.repository = repository
        self.source_currency_factory = source_currency_factory

    async def set_exchange_rate(self, source_url: str) -> None:
        source_currency_manager: SourceCurrencyManagerProtocol = (
            await self.source_currency_factory.make(source_url)
        )
        actual_currency_rate: list[CurrencyDto] = (
            await source_currency_manager.get_source_currency()
        )
        await self.repository.set_exchange_data(
            session=self.session, currency=actual_currency_rate
        )
        await self.session.commit()

    async def get(self): ...
