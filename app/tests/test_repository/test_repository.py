from unittest.mock import AsyncMock, MagicMock

from sqlalchemy.ext.asyncio import AsyncSession
from faker import Faker


from app.dto.dto import CurrencyDto, ValueNameDto
from app.repository.repository import DataBaseRepository
from app.models.currency import Currency


async def test_set_exchange_data(get_mock_db_session: AsyncSession):
    session = get_mock_db_session

    repository = DataBaseRepository()
    faker = Faker()
    count_generate_currency = 10

    fake_currency_list = [
        CurrencyDto(
            char_code=faker.pystr(),
            num_code=faker.random_int(),
            nominal=faker.random_int(),
            name=faker.pystr(),
            value=faker.pyfloat(),
            vunit_rate=faker.pyfloat(),
        )
        for _ in range(count_generate_currency)
    ]

    assert (
        await repository.set_exchange_data(session=session, currency=fake_currency_list)
        is None
    )

    assert session.add.call_count == count_generate_currency


async def test_get_exchange_data_by_char_code(get_mock_db_session: AsyncSession):
    session = get_mock_db_session

    repository = DataBaseRepository()
    faker = Faker()
    mock_currency_dto = CurrencyDto(
        char_code=faker.pystr(),
        num_code=faker.random_int(),
        nominal=faker.random_int(),
        name=faker.pystr(),
        value=faker.pyfloat(),
        vunit_rate=faker.pyfloat(),
    )

    mock_currency = Currency(
        char_code=mock_currency_dto.char_code,
        num_code=mock_currency_dto.num_code,
        nominal=mock_currency_dto.nominal,
        name_rate=mock_currency_dto.name,
        value_rate=mock_currency_dto.value,
        vunit_rate=mock_currency_dto.vunit_rate,
        date="2024-12-02",
        created_at="2024-09-23 23:58:16.688613",
    )
    session.execute.return_value = AsyncMock()
    session.execute.return_value.scalar_one_or_none = MagicMock()
    session.execute.return_value.scalar_one_or_none.return_value = mock_currency

    result_mock_get_exchange_data_by_char_code = (
        await repository.get_exchange_data_by_char_code(
            session=session, value=ValueNameDto(char_code=faker.pystr())
        )
    )

    assert session.execute.call_count == 1
    assert result_mock_get_exchange_data_by_char_code == mock_currency_dto


async def test_not_char_code_get_exchange_data_by_char_code(
    get_mock_db_session: AsyncSession,
):
    session = get_mock_db_session

    repository = DataBaseRepository()
    faker = Faker()
    session.execute.return_value = AsyncMock()
    session.execute.return_value.scalar_one_or_none = MagicMock(return_value=None)

    result_mock_get_exchange_data_by_char_code = (
        await repository.get_exchange_data_by_char_code(
            session=session, value=ValueNameDto(char_code=faker.pystr())
        )
    )

    assert session.execute.call_count == 1
    assert result_mock_get_exchange_data_by_char_code == None
