from typing import Optional

from pydantic import Field, BaseModel


class PostingFBSCustomerAddress(BaseModel):
    """Информация об адресе доставки.

    Attributes:
        address_tail: Адрес в текстовом формате
        city: Город доставки
        comment: Комментарий к заказу
        country: Страна доставки
        district: Район доставки
        latitude: Широта
        longitude: Долгота
        provider_pvz_code: Код пункта выдачи заказов 3PL провайдера
        pvz_code: Код пункта выдачи заказов
        region: Регион доставки
        zip_code: Почтовый индекс получателя
    """
    address_tail: Optional[str] = Field(
        None, description="Адрес в текстовом формате."
    )
    city: Optional[str] = Field(
        None, description="Город доставки."
    )
    comment: Optional[str] = Field(
        None, description="Комментарий к заказу."
    )
    country: Optional[str] = Field(
        None, description="Страна доставки."
    )
    district: Optional[str] = Field(
        None, description="Район доставки."
    )
    latitude: Optional[float] = Field(
        None, description="Широта."
    )
    longitude: Optional[float] = Field(
        None, description="Долгота."
    )
    provider_pvz_code: Optional[str] = Field(
        None, description="Код пункта выдачи заказов 3PL провайдера."
    )
    pvz_code: Optional[int] = Field(
        None, description="Код пункта выдачи заказов."
    )
    region: Optional[str] = Field(
        None, description="Регион доставки."
    )
    zip_code: Optional[str] = Field(
        None, description="Почтовый индекс получателя."
    )
