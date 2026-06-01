"""Схемы метода cargoes_create_info (информация по установке грузомест, v2)."""
from typing import Optional

from pydantic import BaseModel, Field


class CargoesCreateInfoRequest(BaseModel):
    """Параметры запроса информации по установке грузомест.

    Attributes:
        operation_id: Идентификатор операции установки грузомест
    """
    operation_id: str = Field(
        ..., description="Идентификатор операции установки грузомест."
    )


class CargoesCreateInfoItemValidation(BaseModel):
    """Ошибка валидации товара при установке грузомест.

    Attributes:
        cargo_key: Идентификатор грузоместа в запросе
        item: Идентификатор товара
        quant: Размер кванта
        type: Тип ошибки валидации
    """
    cargo_key: Optional[str] = Field(
        None, description="Идентификатор грузоместа в запросе."
    )
    item: Optional[str] = Field(None, description="Идентификатор товара.")
    quant: Optional[int] = Field(None, description="Размер кванта.")
    type: Optional[str] = Field(None, description="Тип ошибки валидации.")


class CargoesCreateInfoErrors(BaseModel):
    """Ошибки установки грузомест.

    Attributes:
        error_reasons: Причины ошибки
        items_validation: Ошибки валидации товаров
    """
    error_reasons: Optional[list[str]] = Field(
        None, description="Причины ошибки."
    )
    items_validation: Optional[list[CargoesCreateInfoItemValidation]] = Field(
        None, description="Ошибки валидации товаров."
    )


class CargoesCreateInfoCargoValue(BaseModel):
    """Идентификатор установленного грузоместа.

    Attributes:
        cargo_id: Идентификатор грузоместа
    """
    cargo_id: Optional[int] = Field(None, description="Идентификатор грузоместа.")


class CargoesCreateInfoCargo(BaseModel):
    """Установленное грузоместо.

    Attributes:
        key: Идентификатор грузоместа в запросе
        value: Идентификатор установленного грузоместа
    """
    key: Optional[str] = Field(
        None, description="Идентификатор грузоместа в запросе."
    )
    value: Optional[CargoesCreateInfoCargoValue] = Field(
        None, description="Идентификатор установленного грузоместа."
    )


class CargoesCreateInfoResult(BaseModel):
    """Результат установки грузомест.

    Attributes:
        cargoes: Установленные грузоместа
    """
    cargoes: Optional[list[CargoesCreateInfoCargo]] = Field(
        None, description="Установленные грузоместа."
    )


class CargoesCreateInfoResponse(BaseModel):
    """Ответ с информацией по установке грузомест.

    Attributes:
        errors: Ошибки операции
        result: Результат установки грузомест
        status: Статус операции
    """
    errors: Optional[CargoesCreateInfoErrors] = Field(
        None, description="Ошибки операции."
    )
    result: Optional[CargoesCreateInfoResult] = Field(
        None, description="Результат установки грузомест."
    )
    status: Optional[str] = Field(None, description="Статус операции.")
