"""https://docs.ozon.ru/api/seller/#operation/ReturnsAPI_ReturnsSettingsUtilizationUpdate"""
from typing import Optional

from pydantic import BaseModel, Field


class ReturnsSettingsUtilizationUpdatePrice(BaseModel):
    """Настройка автоутилизации для одной категории товаров.

    Attributes:
        enabled: Признак включённой автоутилизации
        value: Значение цены
    """
    enabled: Optional[bool] = Field(
        None, description="`true`, если автоутилизация включена."
    )
    value: Optional[int] = Field(
        None, description="Значение цены. Обязательно, если `enabled` равно `true`."
    )


class ReturnsSettingsUtilizationUpdateRequest(BaseModel):
    """Описывает схему запроса на обновление настроек автоутилизации.

    Attributes:
        utilization_price: Настройка автоутилизации для товаров без брака
        utilization_price_defects: Настройка автоутилизации для товаров с браком
    """
    utilization_price: ReturnsSettingsUtilizationUpdatePrice = Field(
        ..., description="Настройка автоутилизации для товаров без брака."
    )
    utilization_price_defects: ReturnsSettingsUtilizationUpdatePrice = Field(
        ..., description="Настройка автоутилизации для товаров с браком."
    )


class ReturnsSettingsUtilizationUpdateResponse(BaseModel):
    """Описывает схему ответа на запрос обновления настроек автоутилизации.

    Notes:
        • При успешном обновлении API возвращает пустой объект.
    """
    pass
