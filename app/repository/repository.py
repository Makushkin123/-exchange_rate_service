from typing import Protocol, Optional


from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select
from app.models.currency import Currency
from app.dto.dto import CurrencyDto, ValueNameDto


class RepositoryProtocol(Protocol):
    @staticmethod
    async def set_exchange_data(
        session: AsyncSession, currency: list[CurrencyDto]
    ) -> None: ...

    @staticmethod
    async def get_exchange_data_by_char_code(
        session: AsyncSession, value: ValueNameDto
    ) -> CurrencyDto: ...


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

    @staticmethod
    async def get_exchange_data_by_char_code(
        session: AsyncSession, value: ValueNameDto
    ) -> Optional[CurrencyDto]:
        result = await session.execute(
            select(Currency).where(Currency.char_code == value.char_code)
        )
        currency: Currency = result.scalar_one_or_none()
        if currency is None:
            return None

        return CurrencyDto(
            char_code=currency.char_code,
            num_code=currency.num_code,
            nominal=currency.nominal,
            name=currency.name_rate,
            value=currency.value_rate,
            vunit_rate=currency.vunit_rate,
        )
