import datetime
from typing import Optional

from pydantic import Field, BaseModel


class PostingFBSTariffication(BaseModel):
    """Информация по тарификации отгрузки.

    Attributes:
        current_tariff_rate: Текущий процент тарификации
        current_tariff_type: Текущий тип тарификации
        current_tariff_charge: Текущая сумма скидки или надбавки
        current_tariff_charge_currency_code: Валюта суммы
        next_tariff_rate: Процент следующего тарифа
        next_tariff_type: Тип следующего тарифа
        next_tariff_charge: Сумма следующего тарифа
        next_tariff_starts_at: Дата начала нового тарифа
        next_tariff_charge_currency_code: Валюта нового тарифа
    """
    current_tariff_rate: float = Field(
        ..., description="Текущий процент тарификации."
    )
    current_tariff_type: str = Field(
        ..., description="Текущий тип тарификации — скидка или надбавка."
    )
    current_tariff_charge: str = Field(
        ..., description="Текущая сумма скидки или надбавки."
    )
    current_tariff_charge_currency_code: str = Field(
        ..., description="Валюта суммы."
    )
    next_tariff_rate: float = Field(
        ..., description="Процент, по которому будет тарифицироваться отправление через указанное в параметре next_tariff_starts_at время."
    )
    next_tariff_type: str = Field(
        ..., description="Тип тарифа, по которому будет тарифицироваться отправление через указанное в параметре next_tariff_starts_at время — скидка или надбавка."
    )
    next_tariff_charge: str = Field(
        ..., description="Сумма скидки или надбавки на следующем шаге тарификации."
    )
    next_tariff_starts_at: Optional[datetime.datetime] = Field(
        None, description="Дата и время, когда начнёт применяться новый тариф."
    )
    next_tariff_charge_currency_code: str = Field(
        ..., description="Валюта нового тарифа."
    )
