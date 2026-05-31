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
        current_tariff_min_charge: Текущая минимальная сумма списания
        next_tariff_rate: Процент следующего тарифа
        next_tariff_type: Тип следующего тарифа
        next_tariff_charge: Сумма следующего тарифа
        next_tariff_starts_at: Дата начала нового тарифа
        next_tariff_charge_currency_code: Валюта нового тарифа
        next_tariff_min_charge: Минимальная сумма списания на следующем шаге тарификации
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
    current_tariff_min_charge: Optional[str] = Field(
        None, description="Текущая минимальная сумма списания."
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
    next_tariff_min_charge: Optional[str] = Field(
        None, description="Минимальная сумма списания на следующем шаге тарификации."
    )


class PostingFBSTarifficationCharge(BaseModel):
    """Денежная сумма шага тарификации.

    Attributes:
        amount: Сумма
        currency: Валюта суммы
    """
    amount: Optional[str] = Field(None, description="Сумма.")
    currency: Optional[str] = Field(None, description="Валюта суммы.")


class PostingFBSTarifficationStep(BaseModel):
    """Шаг тарификации отправления — детальная разбивка калькуляции скидок и надбавок.

    Attributes:
        min_charge: Минимальная сумма списания (нижняя граница итоговой суммы)
        tariff_charge: Максимальная сумма списания (верхняя граница итоговой суммы)
        tariff_deadline_at: Дата и время окончания действия текущего шага тарификации (UTC)
        tariff_rate: Процент, применяемый к стоимости отправления
        tariff_type: Тип шага — скидка (discount) или надбавка/штраф (extra_charge)
    """
    min_charge: Optional[PostingFBSTarifficationCharge] = Field(
        None, description="Минимальная сумма списания — нижняя граница итоговой суммы."
    )
    tariff_charge: Optional[PostingFBSTarifficationCharge] = Field(
        None, description="Максимальная сумма списания — верхняя граница итоговой суммы."
    )
    tariff_deadline_at: Optional[datetime.datetime] = Field(
        None, description="Дата и время окончания действия текущего шага тарификации в формате UTC."
    )
    tariff_rate: Optional[float] = Field(
        None, description="Процент, применяемый к стоимости отправления."
    )
    tariff_type: Optional[str] = Field(
        None, description="Тип шага тарификации — discount (скидка) или extra_charge (надбавка/штраф)."
    )
