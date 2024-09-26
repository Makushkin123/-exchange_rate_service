from typing import Protocol
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.currency import Currency
from app.dto.dto import CurrencyDto


class RepositoryProtocol(Protocol):
    @staticmethod
    async def set_exchange_data(
        session: AsyncSession, currency: list[CurrencyDto]
    ) -> None: ...


class DataBaseRepository:
    @staticmethod
    async def set_exchange_data(
        session: AsyncSession, currency: list[CurrencyDto]
    ) -> None:
        for value_rate in currency:
            session.add(
                Currency(
                    num_code=value_rate.num_code,
                    char_code=value_rate.char_code,
                    nominal=value_rate.nominal,
                    name_rate=value_rate.name,
                    value_rate=value_rate.value,
                    vunit_rate=value_rate.vunit_rate,
                )
            )
