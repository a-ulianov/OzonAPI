"""https://docs.ozon.ru/api/seller/#operation/add-barcode"""
from typing import Optional

from pydantic import BaseModel, Field


class BarcodeAddItem(BaseModel):
    """Штрихкод для SKU.

    Attributes:
        sku: Идентификатор товара
        barcode: Штрихкод для привязки
    """
    sku: int = Field(
        ..., description="Идентификатор товара (SKU)"
    )
    barcode: str = Field(
        ..., description="Штрихкод для привязки"
    )


class BarcodeAddRequest(BaseModel):
    """Описывает схему запроса на добавление штрихкода.

    Attributes:
        barcodes: Список штрихкодов и SKU
    """
    barcodes: list[BarcodeAddItem] = Field(
        ..., description="Список штрихкодов и товаров.",
        min_length=1, max_length=100
    )


class BarcodeAddError(BaseModel):
    """Схема, описывающая ошибку привязки штрихкода.

    Attributes:
        code: Код ошибки
        error: Описание ошибки
        barcode: Штрихкод, который не удалось привязать
        sku: Идентификатор товара, к которому не удалось привязать штрихкод
    """
    code: str = Field(
        ..., description="Код ошибки."
    )
    error: str = Field(
        ..., description="Описание ошибки."
    )
    barcode: str = Field(
        ..., description="Штрихкод, который не удалось привязать."
    )
    sku: int = Field(
        ...,
        description="Идентификатор товара, к которому не удалось привязать штрихкод.",
    )


class BarcodeAddResponse(BaseModel):
    """Ответ сервера, содержащий список ошибок.

    Attributes:
        errors: Список ошибок при привязке штрихкодов
    """
    errors: Optional[list[BarcodeAddError]] = Field(
        default_factory=list, description="Список ошибок."
    )
