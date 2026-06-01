"""Схемы метода product_stairway_discount_by_quantity_set (управление скидкой от количества, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import Stairway


class ProductStairwayDiscountByQuantitySetItem(BaseModel):
    """Настройка скидки от количества для товара.

    Attributes:
        enabled: Признак включения скидки
        sku: Идентификатор товара в системе Ozon — SKU
        stairway: Лестница скидок
    """
    enabled: Optional[bool] = Field(None, description="Признак включения скидки.")
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    stairway: Optional[Stairway] = Field(None, description="Лестница скидок.")


class ProductStairwayDiscountByQuantitySetRequest(BaseModel):
    """Параметры запроса управления скидкой от количества.

    Attributes:
        stairways: Настройки скидок по товарам
        suppress_warnings: Игнорировать предупреждения
    """
    stairways: Optional[list[ProductStairwayDiscountByQuantitySetItem]] = Field(
        None, description="Настройки скидок по товарам."
    )
    suppress_warnings: Optional[bool] = Field(
        None, description="Игнорировать предупреждения."
    )


class ProductStairwayDiscountErrorData(BaseModel):
    """Детализация ошибки или предупреждения.

    Attributes:
        code: Код
        field: Поле
        message: Сообщение
        step: Номер ступени
        value: Значение
    """
    code: Optional[str] = Field(None, description="Код.")
    field: Optional[str] = Field(None, description="Поле.")
    message: Optional[str] = Field(None, description="Сообщение.")
    step: Optional[int] = Field(None, description="Номер ступени.")
    value: Optional[str] = Field(None, description="Значение.")


class ProductStairwayDiscountError(BaseModel):
    """Ошибка или предупреждение по товару.

    Attributes:
        data: Детализация
        sku: Идентификатор товара в системе Ozon — SKU
    """
    data: Optional[list[ProductStairwayDiscountErrorData]] = Field(
        None, description="Детализация."
    )
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )


class ProductStairwayDiscountByQuantitySetResponse(BaseModel):
    """Ответ на управление скидкой от количества.

    Attributes:
        accepted: Признак принятия настроек
        errors: Ошибки
        warnings: Предупреждения
    """
    accepted: Optional[bool] = Field(None, description="Признак принятия настроек.")
    errors: Optional[list[ProductStairwayDiscountError]] = Field(
        None, description="Ошибки."
    )
    warnings: Optional[list[ProductStairwayDiscountError]] = Field(
        None, description="Предупреждения."
    )
