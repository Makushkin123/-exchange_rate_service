import datetime
import uuid

from sqlalchemy import types, text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from app.models.base import Base
from sqlalchemy.sql import func


class Currency(Base):
    __tablename__ = "currency"

    id: Mapped[uuid.UUID] = mapped_column(
        types.Uuid,
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    )
    num_code: Mapped[int]
    char_code: Mapped[str]
    nominal: Mapped[int]
    name_rate: Mapped[str]
    value_rate: Mapped[float]
    vunit_rate: Mapped[float]
    date: Mapped[str] = mapped_column(
        default=datetime.datetime.now().strftime("%Y-%m-%d")
    )
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
