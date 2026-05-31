import datetime
from typing import Optional

from pydantic import BaseModel, Field


class SupplyOrderTimeslot(BaseModel):
    """Интервал поставки заявки FBO.

    Attributes:
        from_: Начало интервала по местному времени (сериализуется как `from`)
        to: Конец интервала по местному времени
    """
    model_config = {'populate_by_name': True}

    from_: Optional[datetime.datetime] = Field(
        None, alias="from", description="Начало интервала по местному времени."
    )
    to: Optional[datetime.datetime] = Field(
        None, description="Конец интервала по местному времени."
    )


class SupplyOrderTimezoneInfo(BaseModel):
    """Информация о часовом поясе интервала поставки.

    Attributes:
        iana_name: Название часового пояса (IANA)
        offset: Смещение часового пояса от UTC-0 в секундах
    """
    iana_name: Optional[str] = Field(
        None, description="Название часового пояса (IANA)."
    )
    offset: Optional[str] = Field(
        None, description="Смещение часового пояса от UTC-0 в секундах."
    )
