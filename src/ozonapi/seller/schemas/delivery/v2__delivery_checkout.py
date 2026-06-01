"""Схемы метода delivery_checkout (доступные варианты доставки, v2)."""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.delivery import DeliverySchema
from .entities import DeliveryDateRange


class DeliveryCheckoutCourierCoordinates(BaseModel):
    """Координаты адреса для курьерской доставки.

    Attributes:
        latitude: Широта
        longitude: Долгота
    """
    latitude: Optional[float] = Field(None, description="Широта.")
    longitude: Optional[float] = Field(None, description="Долгота.")


class DeliveryCheckoutCourier(BaseModel):
    """Параметры курьерской доставки.

    Attributes:
        coordinates: Координаты адреса доставки
    """
    coordinates: Optional[DeliveryCheckoutCourierCoordinates] = Field(
        None, description="Координаты адреса доставки."
    )


class DeliveryCheckoutPickUp(BaseModel):
    """Параметры доставки в точку самовывоза.

    Attributes:
        map_point_id: Идентификатор точки самовывоза на карте
    """
    map_point_id: Optional[int] = Field(
        None, description="Идентификатор точки самовывоза на карте."
    )


class DeliveryCheckoutDeliveryType(BaseModel):
    """Тип доставки в запросе.

    Attributes:
        courier: Курьерская доставка
        pick_up: Доставка в точку самовывоза
    """
    courier: Optional[DeliveryCheckoutCourier] = Field(
        None, description="Курьерская доставка."
    )
    pick_up: Optional[DeliveryCheckoutPickUp] = Field(
        None, description="Доставка в точку самовывоза."
    )


class DeliveryCheckoutItem(BaseModel):
    """Товар в запросе вариантов доставки.

    Attributes:
        offer_id: Идентификатор товара в системе продавца — артикул
        quantity: Количество товара
        sku: Идентификатор товара в системе Ozon — SKU
    """
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    quantity: Optional[int] = Field(None, description="Количество товара.")
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )


class DeliveryCheckoutRequest(BaseModel):
    """Параметры запроса доступных вариантов доставки.

    Attributes:
        buyer_phone: Номер телефона покупателя
        delivery_schema: Схема доставки
        delivery_type: Тип доставки
        items: Список товаров
    """
    buyer_phone: Optional[str] = Field(None, description="Номер телефона покупателя.")
    delivery_schema: Optional[DeliverySchema] = Field(
        None, description="Схема доставки."
    )
    delivery_type: Optional[DeliveryCheckoutDeliveryType] = Field(
        None, description="Тип доставки."
    )
    items: Optional[list[DeliveryCheckoutItem]] = Field(
        None, description="Список товаров."
    )


class DeliveryCheckoutTimeslot(BaseModel):
    """Интервал доставки.

    Attributes:
        client_date_range: Интервал доставки для покупателя
        logistic_date_range: Интервал доставки для логистики
        timeslot_id: Идентификатор интервала
    """
    client_date_range: Optional[DeliveryDateRange] = Field(
        None, description="Интервал доставки для покупателя."
    )
    logistic_date_range: Optional[DeliveryDateRange] = Field(
        None, description="Интервал доставки для логистики."
    )
    timeslot_id: Optional[int] = Field(None, description="Идентификатор интервала.")


class DeliveryCheckoutDeliveryMethod(BaseModel):
    """Метод доставки в ответе.

    Attributes:
        delivery_time_zone_offset: Смещение часового пояса доставки
        delivery_type: Тип доставки
        id: Идентификатор метода доставки
        name: Название метода доставки
        timeslots: Доступные интервалы доставки
        unavailable_reason: Причина недоступности метода доставки
        warehouse_time_zone_offset: Смещение часового пояса склада
    """
    delivery_time_zone_offset: Optional[int] = Field(
        None, description="Смещение часового пояса доставки."
    )
    delivery_type: Optional[str] = Field(None, description="Тип доставки.")
    id: Optional[int] = Field(None, description="Идентификатор метода доставки.")
    name: Optional[str] = Field(None, description="Название метода доставки.")
    timeslots: Optional[list[DeliveryCheckoutTimeslot]] = Field(
        None, description="Доступные интервалы доставки."
    )
    unavailable_reason: Optional[str] = Field(
        None, description="Причина недоступности метода доставки."
    )
    warehouse_time_zone_offset: Optional[int] = Field(
        None, description="Смещение часового пояса склада."
    )


class DeliveryCheckoutSplit(BaseModel):
    """Часть заказа с отдельным вариантом доставки.

    Attributes:
        delivery_method: Метод доставки
        delivery_schema: Схема доставки
        items: Товары в части заказа
        unavailable_reason: Причина недоступности доставки
        warehouse_id: Идентификатор склада
    """
    delivery_method: Optional[DeliveryCheckoutDeliveryMethod] = Field(
        None, description="Метод доставки."
    )
    delivery_schema: Optional[str] = Field(None, description="Схема доставки.")
    items: Optional[list[DeliveryCheckoutItem]] = Field(
        None, description="Товары в части заказа."
    )
    unavailable_reason: Optional[str] = Field(
        None, description="Причина недоступности доставки."
    )
    warehouse_id: Optional[int] = Field(None, description="Идентификатор склада.")


class DeliveryCheckoutResponse(BaseModel):
    """Ответ с доступными вариантами доставки.

    Attributes:
        splits: Части заказа с вариантами доставки
    """
    splits: Optional[list[DeliveryCheckoutSplit]] = Field(
        None, description="Части заказа с вариантами доставки."
    )
