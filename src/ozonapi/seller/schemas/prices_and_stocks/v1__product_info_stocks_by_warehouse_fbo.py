"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetProductInfoStocksByWarehouseFbo"""
from typing import Optional

from pydantic import BaseModel, Field


class ProductInfoStocksByWarehouseFBORequest(BaseModel):
    """Описывает схему запроса информации об остатках на складах FBO (API v1).

    Notes:
        • Фильтровать можно по `skus` и/или `offer_ids`.

    Attributes:
        limit: Количество значений в ответе
        cursor: Указатель для выборки следующих данных
        skus: Идентификаторы товаров в системе Ozon — SKU
        offer_ids: Идентификаторы товаров в системе продавца — артикулы
    """
    limit: int = Field(
        100, description="Количество значений в ответе.", ge=1
    )
    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных."
    )
    skus: Optional[list[str]] = Field(
        None, description="Идентификаторы товаров в системе Ozon — SKU."
    )
    offer_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы товаров в системе продавца — артикулы."
    )


class ProductInfoStocksByWarehouseFBOItem(BaseModel):
    """Данные об остатках определённого товара на складах FBO (API v1).

    Attributes:
        sku: Идентификатор товара в системе Ozon — SKU
        offer_id: Идентификатор товара в системе продавца — артикул
        product_id: Идентификатор товара в системе Ozon
        present: Общее количество товара на складе
        reserved: Количество зарезервированных товаров на складе
        warehouse_id: Идентификатор склада
    """
    sku: Optional[int] = Field(None, description="Идентификатор товара в системе Ozon — SKU.")
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    product_id: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon."
    )
    present: Optional[int] = Field(None, description="Общее количество товара на складе.")
    reserved: Optional[int] = Field(
        None, description="Количество зарезервированных товаров на складе."
    )
    warehouse_id: Optional[int] = Field(None, description="Идентификатор склада.")


class ProductInfoStocksByWarehouseFBOResponse(BaseModel):
    """Описывает схему ответа на запрос об остатках товаров на складах FBO (API v1).

    Attributes:
        products: Массив данных об остатках товаров на складах FBO
        cursor: Указатель для выборки следующих данных
        has_next: Признак, что в ответе вернулась только часть значений
    """
    products: list[ProductInfoStocksByWarehouseFBOItem] = Field(
        default_factory=list, description="Массив данных об остатках товаров на складах FBO."
    )
    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных."
    )
    has_next: Optional[bool] = Field(
        None, description="Признак, что в ответе вернулась только часть значений."
    )
