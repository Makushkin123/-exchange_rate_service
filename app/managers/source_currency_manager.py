import xmltodict
from typing import Protocol
from httpx import AsyncClient


from app.config import settings
from app.dto.dto import CurrencyDto


class SourceCurrencyManagerProtocol(Protocol):
    async def get_source_currency(self) -> list[CurrencyDto]: ...


class SourceCurrencyManagerRussianBank:
    def __init__(self, source_url: str):
        self.source_url = source_url

    async def __get_source_for_url(self) -> str:
        async with AsyncClient() as client:
            response = await client.get(self.source_url)
            return response.text

    @staticmethod
    async def __get_currency_rate(currency_dict: dict) -> list[CurrencyDto]:
        result_currency = []
        for currency in currency_dict["ValCurs"]["Valute"]:
            result_currency.append(
                CurrencyDto(
                    num_code=int(currency["NumCode"]),
                    char_code=currency["CharCode"],
                    nominal=int(currency["Nominal"]),
                    name=currency["Name"],
                    value=float(currency["Value"].replace(",", ".")),
                    vunit_rate=float(currency["VunitRate"].replace(",", ".")),
                )
            )
        return result_currency

    async def get_source_currency(self) -> list[CurrencyDto]:
        xml_currency = await self.__get_source_for_url()
        currency_dict = xmltodict.parse(xml_currency)
        date: list[CurrencyDto] = await self.__get_currency_rate(currency_dict)
        return date


class SourceCurrencyFactory:
    source = {settings.source_url.source_russian_bank: SourceCurrencyManagerRussianBank}

    async def make(self, source_url) -> SourceCurrencyManagerProtocol:
        return self.source[source_url](source_url=source_url)
