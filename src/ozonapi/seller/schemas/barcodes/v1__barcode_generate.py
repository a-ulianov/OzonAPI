"""https://docs.ozon.ru/api/seller/#operation/generate-barcode"""
from typing import Optional

from pydantic import BaseModel, Field


class BarcodeGenerateRequest(BaseModel):
    """Идентификаторы товаров, для которых нужно создать штрихкод.

    Attributes:
        product_ids: Идентификаторы товаров, для которых нужно создать штрихкод (максимум 100)
    """
    product_ids: list[int] = Field(
        ..., description="Идентификаторы товаров, для которых нужно создать штрихкод. Максимум 100.",
        min_length=1, max_length=100,
    )


class BarcodeGenerateError(BaseModel):
    """Схема, описывающая ошибку при создании штрихкода.

    Attributes:
        code: Код ошибки
        error: Описание ошибки
        barcode: Штрихкод, при создании которого произошла ошибка
        product_id: Идентификатор товара, для которого не удалось создать штрихкод
    """
    code: str = Field(..., description="Код ошибки.")
    error: str = Field(..., description="Описание ошибки.")
    barcode: str = Field(
        ..., description="Штрихкод, при создании которого произошла ошибка."
    )
    product_id: int = Field(
        ..., description="Идентификатор товара, для которого не удалось создать штрихкод.",
    )


class BarcodeGenerateResponse(BaseModel):
    """Описывает схему ответа от сервера, содержащую список ошибок при генерации штрихкодов.

    Attributes:
        errors: Список ошибок при создании штрихкодов
    """
    errors: Optional[list[BarcodeGenerateError]] = Field(
        default_factory=list, description="Ошибки при создании штрихкода."
    )
