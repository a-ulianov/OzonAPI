"""https://docs.ozon.ru/api/seller/#operation/ReturnsAPI_ReturnsSettingsUtilizationInfo"""
from typing import Optional

from pydantic import BaseModel, Field


class UtilizationMoney(BaseModel):
    """Денежная сумма настроек автоутилизации.

    Attributes:
        amount: Сумма
        currency: Валюта
    """
    amount: Optional[str] = Field(
        None, description="Сумма."
    )
    currency: Optional[str] = Field(
        None, description="Валюта."
    )


class ReturnsSettingsUtilizationInfoSettings(BaseModel):
    """Настройки автоутилизации.

    Attributes:
        utilization_price: Стоимость утилизации для товаров без брака
        utilization_price_defects: Стоимость утилизации для товаров с браком
    """
    utilization_price: Optional[UtilizationMoney] = Field(
        None, description="Стоимость утилизации для товаров без брака."
    )
    utilization_price_defects: Optional[UtilizationMoney] = Field(
        None, description="Стоимость утилизации для товаров с браком."
    )


class ReturnsSettingsUtilizationInfoResponse(BaseModel):
    """Описывает схему ответа на запрос настроек автоутилизации.

    Attributes:
        min_price: Минимальная стоимость утилизации
        utilization_settings: Настройки автоутилизации
    """
    min_price: Optional[UtilizationMoney] = Field(
        None, description="Минимальная стоимость утилизации."
    )
    utilization_settings: Optional[ReturnsSettingsUtilizationInfoSettings] = Field(
        None, description="Настройки автоутилизации."
    )
