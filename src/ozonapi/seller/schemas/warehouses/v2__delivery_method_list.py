"""https://docs.ozon.ru/api/seller/#operation/WarehouseAPI_DeliveryMethodListV2"""
import datetime
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.delivery import DeliveryMethodStatus, SortDir


class DeliveryMethodListFilter(BaseModel):
    """Фильтр для поиска методов доставки (API v2).

    Attributes:
        delivery_method_ids: Идентификаторы методов доставки
        provider_ids: Идентификаторы служб доставки
        status: Статусы методов доставки
        warehouse_ids: Идентификаторы складов
    """
    delivery_method_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы методов доставки."
    )
    provider_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы служб доставки."
    )
    status: Optional[list[DeliveryMethodStatus]] = Field(
        None, description="Статусы методов доставки."
    )
    warehouse_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы складов."
    )


class DeliveryMethodListRequest(BaseModel):
    """Схема запроса о списке методов доставки склада (API v2).

    Attributes:
        limit: Количество элементов в ответе
        cursor: Указатель для выборки следующих данных
        filter: Фильтр для поиска методов доставки
        sort_dir: Направление сортировки
    """
    limit: int = Field(
        100, description="Количество элементов в ответе.", ge=1
    )
    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных."
    )
    filter: Optional[DeliveryMethodListFilter] = Field(
        None, description="Фильтр для поиска методов доставки."
    )
    sort_dir: Optional[SortDir] = Field(
        None, description="Направление сортировки."
    )


class DeliveryMethodListAddressCoordinates(BaseModel):
    """Координаты адреса DropOff-пункта.

    Attributes:
        latitude: Широта
        longitude: Долгота
    """
    latitude: Optional[float] = Field(None, description="Широта.")
    longitude: Optional[float] = Field(None, description="Долгота.")


class DeliveryMethodListDropOffPoint(BaseModel):
    """DropOff-пункт метода доставки.

    Attributes:
        address: Адрес пункта
        address_coordinates: Координаты адреса
        code: Код пункта
        name: Название пункта
    """
    address: Optional[str] = Field(None, description="Адрес пункта.")
    address_coordinates: Optional[DeliveryMethodListAddressCoordinates] = Field(
        None, description="Координаты адреса."
    )
    code: Optional[str] = Field(None, description="Код пункта.")
    name: Optional[str] = Field(None, description="Название пункта.")


class DeliveryMethodListItem(BaseModel):
    """Модель элемента списка методов доставки (API v2).

    Attributes:
        id: Идентификатор метода доставки
        name: Название метода доставки
        status: Статус метода доставки
        warehouse_id: Идентификатор склада
        provider_id: Идентификатор службы доставки
        template_id: Идентификатор услуги по доставке заказа
        cutoff: Время, до которого нужно собрать заказ
        sla_cut_in: Минимальное время на сборку заказа в минутах
        is_express: Признак экспресс-доставки
        tpl_integration_type: Тип интеграции со службой доставки
        tpl_dropoff_point: DropOff-пункт метода доставки
        created_at: Дата и время создания метода доставки
        updated_at: Дата и время последнего обновления метода доставки
    """
    id: Optional[int] = Field(None, description="Идентификатор метода доставки.")
    name: Optional[str] = Field(None, description="Название метода доставки.")
    status: Optional[str] = Field(None, description="Статус метода доставки.")
    warehouse_id: Optional[int] = Field(None, description="Идентификатор склада.")
    provider_id: Optional[int] = Field(None, description="Идентификатор службы доставки.")
    template_id: Optional[int] = Field(None, description="Идентификатор услуги по доставке заказа.")
    cutoff: Optional[str] = Field(
        None, description="Время, до которого продавцу нужно собрать заказ."
    )
    sla_cut_in: Optional[int] = Field(
        None, description="Минимальное время на сборку заказа в минутах."
    )
    is_express: Optional[bool] = Field(None, description="Признак экспресс-доставки.")
    tpl_integration_type: Optional[str] = Field(
        None, description="Тип интеграции со службой доставки."
    )
    tpl_dropoff_point: Optional[DeliveryMethodListDropOffPoint] = Field(
        None, description="DropOff-пункт метода доставки."
    )
    created_at: Optional[datetime.datetime] = Field(
        None, description="Дата и время создания метода доставки."
    )
    updated_at: Optional[datetime.datetime] = Field(
        None, description="Дата и время последнего обновления метода доставки."
    )


class DeliveryMethodListResponse(BaseModel):
    """Описывает ответ на запрос о списке методов доставки склада (API v2).

    Attributes:
        delivery_methods: Список методов доставки
        cursor: Указатель для выборки следующих данных
        has_next: Признак, что в ответе вернулась только часть значений
    """
    delivery_methods: list[DeliveryMethodListItem] = Field(
        default_factory=list, description="Список методов доставки."
    )
    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных."
    )
    has_next: Optional[bool] = Field(
        None, description="Признак, что в ответе вернулась только часть значений."
    )
