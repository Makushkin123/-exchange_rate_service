from typing import Generator
from unittest.mock import MagicMock, AsyncMock

import pytest
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.fixture(scope="function")
def get_mock_db_session() -> Generator[AsyncSession, None, None]:
    """
    Fixture that create mock session db sqlalchemy.
    """
    session = AsyncMock(spec=AsyncSession)
    yield session
