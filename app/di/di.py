from fastapi import Depends

from app.service.exchange_rate_service import (
    ExchangeRateServiceProtocol,
    ExchangeRateService,
)
from app.models.dp_helper import db_helper
from app.repository.repository import RepositoryProtocol, DataBaseRepository
from app.managers.source_currency_manager import SourceCurrencyFactory


# creating objects for periodic tasks
def get_database_repository() -> RepositoryProtocol:
    return DataBaseRepository()


def get_source_currency_factory() -> SourceCurrencyFactory:
    return SourceCurrencyFactory()


def get_exchange_rate_service(
    session=Depends(db_helper.session_getter_context_manager),
    repository=Depends(get_database_repository),
    source_currency_factory=Depends(get_source_currency_factory),
) -> ExchangeRateServiceProtocol:
    return ExchangeRateService(
        session=session,
        repository=repository,
        source_currency_factory=source_currency_factory,
    )
