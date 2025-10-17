"""https://docs.ozon.ru/api/seller/#operation/WarehouseAPI_DeliveryMethodList"""
import datetime
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.delivery import DeliveryMethodStatus
from ..base import BaseResponseHasNext, BaseRequestOffset, BaseDeliveryMethod


class DeliveryMethodListFilter(BaseModel):
    """Фильтр для поиска методов доставки.

    Attributes:
        provider_id (int): Идентификатор службы доставки (опционально)
        warehouse_id (int): Идентификатор склада, можно получить с помощью метода warehouse_list() (опционально)
        status (DeliveryMethodStatus): Статус метода доставки (опционально)
    """
    provider_id: Optional[int] = Field(
        None, description="Идентификатор службы доставки."
    )
    status: Optional[DeliveryMethodStatus] = Field(
        None, description="Статус метода доставки."
    )
    warehouse_id: Optional[int] = Field(
        None, description="Идентификатор склада. Можно получить с помощью метода warehouse_list()."
    )


class DeliveryMethodListRequest(BaseRequestOffset):
    """Схема запроса о списке методов доставки склада.

    Attributes:
        filter (DeliveryMethodListFilter): Фильтр для поиска методов доставки (опционально)
        limit (int): Количество элементов в ответе (опционально, максимум — 50/минимум — 1)
        offset (int): Количество элементов, которое будет пропущено в ответе (опционально)
    """
    filter: Optional[DeliveryMethodListFilter] = Field(
        None, description="Фильтр для поиска методов доставки."
    )
    limit: Optional[int] = Field(
        50, description="Количество элементов в ответе. Максимум — 50, минимум — 1.",
        ge=1, le=50
    )


class DeliveryMethodListItem(BaseDeliveryMethod):
    """Модель элемента списка методов доставки.

    Attributes:
        company_id: Идентификатор продавца
        created_at: Дата и время создания метода доставки
        cutoff: Время сборки заказа
        provider_id: Идентификатор службы доставки
        sla_cut_in: Минимальное время на сборку заказа
        status: Статус метода доставки
        template_id: Идентификатор услуги по доставке заказа
        updated_at: Дата и время последнего обновления метода доставки
    """
    company_id: int = Field(
        ..., description="Идентификатор продавца."
    )
    created_at: datetime.datetime = Field(
        ..., description="Дата и время создания метода доставки."
    )
    cutoff: str = Field(
        ..., description="Время, до которого продавцу нужно собрать заказ."
    )
    provider_id: int = Field(
        ..., description="Идентификатор службы доставки."
    )
    sla_cut_in: int = Field(
        ..., description="Минимальное время на сборку заказа в минутах в соответствии с настройками склада."
    )
    status: DeliveryMethodStatus = Field(
        DeliveryMethodStatus.ACTIVE, description="Статус метода доставки."
    )
    template_id: int = Field(
        ..., description="Идентификатор услуги по доставке заказа."
    )
    updated_at: datetime.datetime = Field(
        ..., description="Дата и время последнего обновления метода метода доставки."
    )


class DeliveryMethodListResponse(BaseResponseHasNext):
    """Модель, описывающая результат ответа на запрос о списке методов доставки склада.

    Attributes:
        has_next (bool): Признак, что в ответе вернулась только часть значений
        result (list[DeliveryMethodListItem]): Список методов доставки
    """
    result: list[DeliveryMethodListItem] = Field(
        default_factory=list, description="Список методов доставки."
    )