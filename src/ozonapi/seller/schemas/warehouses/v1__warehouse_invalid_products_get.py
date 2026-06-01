"""Схемы метода warehouse_invalid_products_get (товары с ограничениями, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class WarehouseInvalidProductsGetRequest(BaseModel):
    """Параметры запроса товаров с ограничениями по доставке.

    Attributes:
        last_id: Идентификатор последнего значения для пагинации
        warehouse_id: Идентификатор склада
    """
    last_id: Optional[int] = Field(
        None, description="Идентификатор последнего значения для пагинации."
    )
    warehouse_id: int = Field(..., description="Идентификатор склада.")


class WarehouseInvalidProductItemSize(BaseModel):
    """Габариты товара.

    Attributes:
        height_mm: Высота в миллиметрах
        length_mm: Длина в миллиметрах
        width_mm: Ширина в миллиметрах
    """
    height_mm: Optional[int] = Field(None, description="Высота в миллиметрах.")
    length_mm: Optional[int] = Field(None, description="Длина в миллиметрах.")
    width_mm: Optional[int] = Field(None, description="Ширина в миллиметрах.")


class WarehouseInvalidProductItem(BaseModel):
    """Товар с ограничением по доставке.

    Attributes:
        size: Габариты товара
        sku: Идентификатор товара в системе Ozon — SKU
        weight_g: Вес товара в граммах
    """
    size: Optional[WarehouseInvalidProductItemSize] = Field(
        None, description="Габариты товара."
    )
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    weight_g: Optional[float] = Field(None, description="Вес товара в граммах.")


class WarehouseInvalidProductMoney(BaseModel):
    """Денежное значение ограничения.

    Attributes:
        currency: Код валюты
        value: Значение
    """
    currency: Optional[str] = Field(None, description="Код валюты.")
    value: Optional[float] = Field(None, description="Значение.")


class WarehouseInvalidProductValidationError(BaseModel):
    """Ошибка валидации товара.

    Attributes:
        characteristic: Характеристика с ограничением
        restriction_price: Ценовое ограничение
        restriction_vwc: Ограничение по объёмному весу
        template_id: Идентификатор шаблона
        type: Тип ошибки валидации
    """
    characteristic: Optional[str] = Field(
        None, description="Характеристика с ограничением."
    )
    restriction_price: Optional[WarehouseInvalidProductMoney] = Field(
        None, description="Ценовое ограничение."
    )
    restriction_vwc: Optional[float] = Field(
        None, description="Ограничение по объёмному весу."
    )
    template_id: Optional[int] = Field(None, description="Идентификатор шаблона.")
    type: Optional[str] = Field(None, description="Тип ошибки валидации.")


class WarehouseInvalidProductValidationResult(BaseModel):
    """Результат проверки товара.

    Attributes:
        item: Товар
        state: Состояние товара
        validation_errors: Ошибки валидации
    """
    item: Optional[WarehouseInvalidProductItem] = Field(None, description="Товар.")
    state: Optional[str] = Field(None, description="Состояние товара.")
    validation_errors: Optional[list[WarehouseInvalidProductValidationError]] = Field(
        None, description="Ошибки валидации."
    )


class WarehouseInvalidProductsGetResponse(BaseModel):
    """Ответ со списком товаров с ограничениями по доставке.

    Attributes:
        has_next: Признак наличия следующей страницы
        last_id: Идентификатор последнего значения для пагинации
        validation_results: Результаты проверки товаров
        warehouse_id: Идентификатор склада
    """
    has_next: Optional[bool] = Field(
        None, description="Признак наличия следующей страницы."
    )
    last_id: Optional[int] = Field(
        None, description="Идентификатор последнего значения для пагинации."
    )
    validation_results: Optional[list[WarehouseInvalidProductValidationResult]] = Field(
        None, description="Результаты проверки товаров."
    )
    warehouse_id: Optional[int] = Field(None, description="Идентификатор склада.")
