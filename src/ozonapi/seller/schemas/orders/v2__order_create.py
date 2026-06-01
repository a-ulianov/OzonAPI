"""Схемы метода order_create (создание заказа, v2)."""
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from ...common.enumerations.orders import OrderDeliverySchema, OrderDeliveryType


class OrderCreateBuyer(BaseModel):
    """Данные покупателя.

    Attributes:
        first_name: Имя покупателя
        last_name: Фамилия покупателя
        middle_name: Отчество покупателя
        phone: Телефон покупателя
    """
    first_name: Optional[str] = Field(None, description="Имя покупателя.")
    last_name: Optional[str] = Field(None, description="Фамилия покупателя.")
    middle_name: Optional[str] = Field(None, description="Отчество покупателя.")
    phone: Optional[str] = Field(None, description="Телефон покупателя.")


class OrderCreateCourierCoordinates(BaseModel):
    """Координаты адреса доставки курьером.

    Attributes:
        latitude: Широта
        longitude: Долгота
    """
    latitude: Optional[float] = Field(None, description="Широта.")
    longitude: Optional[float] = Field(None, description="Долгота.")


class OrderCreateDeliveryCourier(BaseModel):
    """Адрес доставки курьером.

    Attributes:
        apartment: Квартира
        city: Город
        comment: Комментарий к адресу
        coordinates: Координаты адреса
        country: Страна
        entrance: Подъезд
        floor: Этаж
        house_number: Номер дома
        intercom: Домофон
        region: Регион
        street: Улица
        zip_code: Почтовый индекс
    """
    apartment: Optional[str] = Field(None, description="Квартира.")
    city: Optional[str] = Field(None, description="Город.")
    comment: Optional[str] = Field(None, description="Комментарий к адресу.")
    coordinates: Optional[OrderCreateCourierCoordinates] = Field(
        None, description="Координаты адреса."
    )
    country: Optional[str] = Field(None, description="Страна.")
    entrance: Optional[str] = Field(None, description="Подъезд.")
    floor: Optional[str] = Field(None, description="Этаж.")
    house_number: Optional[str] = Field(None, description="Номер дома.")
    intercom: Optional[str] = Field(None, description="Домофон.")
    region: Optional[str] = Field(None, description="Регион.")
    street: Optional[str] = Field(None, description="Улица.")
    zip_code: Optional[str] = Field(None, description="Почтовый индекс.")


class OrderCreateDeliveryPickUp(BaseModel):
    """Пункт выдачи доставки.

    Attributes:
        map_point_id: Идентификатор точки на карте
    """
    map_point_id: Optional[int] = Field(
        None, description="Идентификатор точки на карте."
    )


class OrderCreateDelivery(BaseModel):
    """Данные о доставке заказа.

    Attributes:
        courier: Адрес доставки курьером
        pick_up: Пункт выдачи доставки
    """
    courier: Optional[OrderCreateDeliveryCourier] = Field(
        None, description="Адрес доставки курьером."
    )
    pick_up: Optional[OrderCreateDeliveryPickUp] = Field(
        None, description="Пункт выдачи доставки."
    )


class OrderCreateRecipient(BaseModel):
    """Данные получателя заказа.

    Attributes:
        recipient_first_name: Имя получателя
        recipient_last_name: Фамилия получателя
        recipient_middle_name: Отчество получателя
        recipient_phone: Телефон получателя
    """
    recipient_first_name: Optional[str] = Field(None, description="Имя получателя.")
    recipient_last_name: Optional[str] = Field(
        None, description="Фамилия получателя."
    )
    recipient_middle_name: Optional[str] = Field(
        None, description="Отчество получателя."
    )
    recipient_phone: Optional[str] = Field(None, description="Телефон получателя.")


class OrderCreatePrice(BaseModel):
    """Цена в денежном формате.

    Attributes:
        currency_code: Код валюты
        nanos: Дробная часть суммы в нанорублях
        units: Целая часть суммы
    """
    currency_code: Optional[str] = Field(None, description="Код валюты.")
    nanos: Optional[int] = Field(
        None, description="Дробная часть суммы в нанорублях."
    )
    units: Optional[int] = Field(None, description="Целая часть суммы.")


class OrderCreateDateRange(BaseModel):
    """Диапазон дат логистики.

    Attributes:
        from_: Начало диапазона
        to_: Конец диапазона
    """
    model_config = ConfigDict(populate_by_name=True)

    from_: Optional[str] = Field(
        None, alias="from", description="Начало диапазона."
    )
    to_: Optional[str] = Field(None, alias="to", description="Конец диапазона.")


class OrderCreateDeliveryMethod(BaseModel):
    """Метод доставки разбиения заказа.

    Attributes:
        delivery_method_id: Идентификатор метода доставки
        delivery_type: Тип доставки
        logistic_date_range: Диапазон дат логистики
        price: Стоимость доставки
        timeslot_id: Идентификатор таймслота
    """
    delivery_method_id: Optional[int] = Field(
        None, description="Идентификатор метода доставки."
    )
    delivery_type: Optional[OrderDeliveryType] = Field(
        None, description="Тип доставки."
    )
    logistic_date_range: Optional[OrderCreateDateRange] = Field(
        None, description="Диапазон дат логистики."
    )
    price: Optional[OrderCreatePrice] = Field(
        None, description="Стоимость доставки."
    )
    timeslot_id: Optional[int] = Field(
        None, description="Идентификатор таймслота."
    )


class OrderCreateItem(BaseModel):
    """Товар разбиения заказа.

    Attributes:
        offer_id: Идентификатор товара в системе продавца — артикул
        price: Цена товара
        quantity: Количество товара
        sku: Идентификатор товара в системе Ozon — SKU
    """
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    price: Optional[OrderCreatePrice] = Field(None, description="Цена товара.")
    quantity: Optional[int] = Field(None, description="Количество товара.")
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )


class OrderCreateSplit(BaseModel):
    """Разбиение заказа на отправления.

    Attributes:
        delivery_method: Метод доставки разбиения
        items: Товары разбиения
        warehouse_id: Идентификатор склада
    """
    delivery_method: Optional[OrderCreateDeliveryMethod] = Field(
        None, description="Метод доставки разбиения."
    )
    items: Optional[list[OrderCreateItem]] = Field(
        None, description="Товары разбиения."
    )
    warehouse_id: Optional[int] = Field(
        None, description="Идентификатор склада."
    )


class OrderCreateRequest(BaseModel):
    """Параметры запроса создания заказа.

    Attributes:
        buyer: Данные покупателя
        delivery: Данные о доставке
        delivery_schema: Схема доставки
        recipient: Данные получателя
        splits: Разбиения заказа на отправления
    """
    buyer: Optional[OrderCreateBuyer] = Field(
        None, description="Данные покупателя."
    )
    delivery: Optional[OrderCreateDelivery] = Field(
        None, description="Данные о доставке."
    )
    delivery_schema: Optional[OrderDeliverySchema] = Field(
        None, description="Схема доставки."
    )
    recipient: Optional[OrderCreateRecipient] = Field(
        None, description="Данные получателя."
    )
    splits: Optional[list[OrderCreateSplit]] = Field(
        None, description="Разбиения заказа на отправления."
    )


class OrderCreateResponse(BaseModel):
    """Ответ на создание заказа.

    Attributes:
        order_number: Номер созданного заказа
        postings: Номера созданных отправлений
    """
    order_number: Optional[str] = Field(
        None, description="Номер созданного заказа."
    )
    postings: Optional[list[str]] = Field(
        None, description="Номера созданных отправлений."
    )
