from pydantic import BaseModel


class ValueNameDto(BaseModel):
    char_code: str


class CurrencyDto(ValueNameDto):
    num_code: int
    nominal: int
    name: str
    value: float
    vunit_rate: float

    class ConfigDict:
        populate_by_name = True
        from_attributes = True
