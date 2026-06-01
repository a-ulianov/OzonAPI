"""Схемы метода delivery_method_return_settings_get (возвратные настройки, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class DeliveryMethodReturnSettingsRequest(BaseModel):
    """Параметры запроса возвратных настроек метода доставки.

    Attributes:
        delivery_method_id: Идентификатор метода доставки
    """
    delivery_method_id: int = Field(
        ..., description="Идентификатор метода доставки."
    )


class DeliveryMethodReturnSettingsCourierDetails(BaseModel):
    """Детали возврата курьером.

    Attributes:
        contact_days: Число дней для связи
    """
    contact_days: Optional[int] = Field(None, description="Число дней для связи.")


class DeliveryMethodReturnSettingsTransportCompanyDetails(BaseModel):
    """Детали возврата транспортной компанией.

    Attributes:
        transport_company_names: Названия транспортных компаний
        zipcode: Почтовый индекс
    """
    transport_company_names: Optional[list[str]] = Field(
        None, description="Названия транспортных компаний."
    )
    zipcode: Optional[str] = Field(None, description="Почтовый индекс.")


class DeliveryMethodReturnSetting(BaseModel):
    """Возвратные настройки метода доставки.

    Attributes:
        courier_details: Детали возврата курьером
        post_office_zipcode: Почтовый индекс отделения
        transport_company_details: Детали возврата транспортной компанией
    """
    courier_details: Optional[DeliveryMethodReturnSettingsCourierDetails] = Field(
        None, description="Детали возврата курьером."
    )
    post_office_zipcode: Optional[str] = Field(
        None, description="Почтовый индекс отделения."
    )
    transport_company_details: Optional[
        DeliveryMethodReturnSettingsTransportCompanyDetails
    ] = Field(None, description="Детали возврата транспортной компанией.")


class DeliveryMethodReturnSettingsResponse(BaseModel):
    """Ответ с возвратными настройками метода доставки.

    Attributes:
        settings: Возвратные настройки
    """
    settings: Optional[DeliveryMethodReturnSetting] = Field(
        None, description="Возвратные настройки."
    )
