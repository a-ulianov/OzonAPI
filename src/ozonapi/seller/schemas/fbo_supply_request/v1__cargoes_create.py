"""Схемы метода cargoes_create (установка грузомест, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.fbo_supply_request import CargoType


class CargoesCreateItem(BaseModel):
    """Товар внутри грузоместа.

    Attributes:
        barcode: Штрихкод товара
        expires_at: Срок годности товара
        offer_id: Идентификатор товара в системе продавца — артикул
        quant: Размер кванта
        quantity: Количество товара
    """
    barcode: Optional[str] = Field(None, description="Штрихкод товара.")
    expires_at: Optional[str] = Field(None, description="Срок годности товара.")
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    quant: Optional[int] = Field(None, description="Размер кванта.")
    quantity: Optional[int] = Field(None, description="Количество товара.")


class CargoesCreateCargoValue(BaseModel):
    """Содержимое грузоместа.

    Attributes:
        items: Товары в грузоместе
        type: Тип грузоместа
    """
    items: Optional[list[CargoesCreateItem]] = Field(
        None, description="Товары в грузоместе."
    )
    type: Optional[CargoType] = Field(None, description="Тип грузоместа.")


class CargoesCreateCargo(BaseModel):
    """Грузоместо для установки.

    Attributes:
        key: Идентификатор грузоместа в запросе
        value: Содержимое грузоместа
    """
    key: Optional[str] = Field(
        None, description="Идентификатор грузоместа в запросе."
    )
    value: Optional[CargoesCreateCargoValue] = Field(
        None, description="Содержимое грузоместа."
    )


class CargoesCreateRequest(BaseModel):
    """Параметры запроса установки грузомест.

    Attributes:
        cargoes: Список грузомест
        delete_current_version: Удалить ранее установленные грузоместа
        supply_id: Идентификатор поставки
    """
    cargoes: Optional[list[CargoesCreateCargo]] = Field(
        None, description="Список грузомест."
    )
    delete_current_version: Optional[bool] = Field(
        None, description="`true`, если нужно удалить предыдущие грузоместа."
    )
    supply_id: int = Field(..., description="Идентификатор поставки.")


class CargoesCreateItemValidation(BaseModel):
    """Ошибка валидации товара при установке грузомест.

    Attributes:
        barcode: Штрихкод товара
        cargo_key: Идентификатор грузоместа в запросе
        quant: Размер кванта
        type: Тип ошибки валидации
    """
    barcode: Optional[str] = Field(None, description="Штрихкод товара.")
    cargo_key: Optional[str] = Field(
        None, description="Идентификатор грузоместа в запросе."
    )
    quant: Optional[int] = Field(None, description="Размер кванта.")
    type: Optional[str] = Field(None, description="Тип ошибки валидации.")


class CargoesCreateErrors(BaseModel):
    """Ошибки установки грузомест.

    Attributes:
        error_reasons: Причины ошибки
        items_validation: Ошибки валидации товаров
    """
    error_reasons: Optional[list[str]] = Field(
        None, description="Причины ошибки."
    )
    items_validation: Optional[list[CargoesCreateItemValidation]] = Field(
        None, description="Ошибки валидации товаров."
    )


class CargoesCreateResponse(BaseModel):
    """Ответ на установку грузомест.

    Attributes:
        operation_id: Идентификатор операции
        errors: Ошибки операции
    """
    operation_id: Optional[str] = Field(
        None, description="Идентификатор операции."
    )
    errors: Optional[CargoesCreateErrors] = Field(
        None, description="Ошибки операции."
    )
