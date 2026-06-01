"""Схемы метода product_digital_stocks_import (обновление остатков цифровых товаров, v1)."""
from pydantic import BaseModel, Field


class ProductDigitalStocksImportStock(BaseModel):
    """Данные об остатке цифрового товара.

    Attributes:
        offer_id: Идентификатор товара в системе продавца — артикул
        stock: Количество товара в наличии
    """
    offer_id: str = Field(..., description="Идентификатор товара в системе продавца — артикул.")
    stock: int = Field(..., description="Количество товара в наличии.")


class ProductDigitalStocksImportRequest(BaseModel):
    """Параметры запроса обновления остатков цифровых товаров.

    Attributes:
        stocks: Данные об остатках
    """
    stocks: list[ProductDigitalStocksImportStock] = Field(
        ..., description="Данные об остатках."
    )


class ProductDigitalStocksImportError(BaseModel):
    """Ошибка обновления остатка.

    Attributes:
        code: Код ошибки
        message: Текст ошибки
    """
    code: str = Field("", description="Код ошибки.")
    message: str = Field("", description="Текст ошибки.")


class ProductDigitalStocksImportStatus(BaseModel):
    """Статус обновления остатка товара.

    Attributes:
        errors: Ошибки обновления
        offer_id: Идентификатор товара в системе продавца — артикул
        product_id: Идентификатор товара в системе Ozon — product_id
        sku: Идентификатор товара в системе Ozon — SKU
        updated: `true`, если остаток обновлён
    """
    errors: list[ProductDigitalStocksImportError] = Field(
        default_factory=list, description="Ошибки обновления."
    )
    offer_id: str = Field("", description="Идентификатор товара в системе продавца — артикул.")
    product_id: int = Field(0, description="Идентификатор товара в системе Ozon — product_id.")
    sku: int = Field(0, description="Идентификатор товара в системе Ozon — SKU.")
    updated: bool = Field(False, description="`true`, если остаток обновлён.")


class ProductDigitalStocksImportResponse(BaseModel):
    """Ответ на обновление остатков цифровых товаров.

    Attributes:
        status: Статусы обновления остатков
    """
    status: list[ProductDigitalStocksImportStatus] = Field(
        default_factory=list, description="Статусы обновления остатков."
    )
