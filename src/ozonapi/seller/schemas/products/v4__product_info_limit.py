"""https://docs.ozon.ru/api/seller/?__rr=1#operation/ProductAPI_GetUploadQuota"""
import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ProductInfoLimitDailyCreate(BaseModel):
    """Суточный лимит на создание товаров.

    Attributes:
        limit: Количество товаров, которое можно создать за сутки (если значение -1, лимит не ограничен)
        reset_at: Время в формате UTC, когда сбросится значение счётчика за текущие сутки
        usage: Сколько товаров создано за текущие сутки
    """
    limit: int = Field(
        ..., description="Количество товаров, которое можно создать за сутки (если значение -1, лимит не ограничен)."
    )
    reset_at: datetime.datetime = Field(
        ..., description="Время в формате UTC, когда сбросится значение счётчика за текущие сутки."
    )
    usage: int = Field(
        ..., description="Сколько товаров создано за текущие сутки."
    )


class ProductInfoLimitDailyUpdate(BaseModel):
    """Суточный лимит на обновление товаров.

    Attributes:
        limit: Количество товаров, которое можно обновить за сутки (если значение -1, лимит не ограничен)
        reset_at: Время в формате UTC, когда сбросится значение счётчика за текущие сутки
        usage: Сколько товаров обновлено за текущие сутки
    """
    limit: int = Field(
        ..., description="Количество товаров, которое можно обновить за сутки (если значение -1, лимит не ограничен)."
    )
    reset_at: datetime.datetime = Field(
        ..., description="Время в формате UTC, когда сбросится значение счётчика за текущие сутки."
    )
    usage: int = Field(
        ..., description="Сколько товаров обновлено за текущие сутки."
    )


class ProductInfoLimitTotal(BaseModel):
    """Лимит на ассортимент.

    Attributes:
        limit: Количество товаров, которое можно создать в личном кабинете (если значение -1, лимит не ограничен)
        usage: Сколько товаров уже создано
    """
    limit: int = Field(
        ..., description="Количество товаров, которое можно создать в личном кабинете (если значение -1, лимит не ограничен)."
    )
    usage: int = Field(
        ..., description="Сколько товаров уже создано."
    )


class ProductInfoLimitOperationLimits(BaseModel):
    """Доступный лимит на работу с товарами (поминутный).

    Attributes:
        limit: Количество товаров, которое можно создать за минуту
        limit_type: Тип текущего лимита (UNSPECIFIED — не указан, RATE_LIMIT_PER_MINUTE — поминутный лимит)
    """
    limit: Optional[int] = Field(
        None, description="Количество товаров, которое можно создать за минуту."
    )
    limit_type: Optional[str] = Field(
        None,
        description="Тип текущего лимита: UNSPECIFIED — не указан; RATE_LIMIT_PER_MINUTE — поминутный лимит."
    )


class ProductInfoLimitResponse(BaseModel):
    """Описывает схему ответа на запрос об установленных и доступных лимитах на ассортимент, создание и обновление товаров.

    Attributes:
        daily_create: Суточный лимит на создание товаров
        daily_update: Суточный лимит на обновление товаров
        operation_limits: Доступный лимит на работу с товарами (поминутный)
        total: Лимит на ассортимент
    """
    daily_create: ProductInfoLimitDailyCreate = Field(
        ..., description="Суточный лимит на создание товаров."
    )
    daily_update: ProductInfoLimitDailyUpdate = Field(
        ..., description="Суточный лимит на обновление товаров."
    )
    operation_limits: Optional[ProductInfoLimitOperationLimits] = Field(
        None, description="Доступный лимит на работу с товарами (поминутный)."
    )
    total: ProductInfoLimitTotal = Field(
        ..., description="Лимит на ассортимент."
    )