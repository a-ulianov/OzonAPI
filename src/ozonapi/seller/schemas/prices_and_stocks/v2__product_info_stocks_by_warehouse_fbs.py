"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductStocksByWarehouseFbsV2"""
from typing import Optional

from pydantic import BaseModel, Field


class ProductInfoStocksByWarehouseFBSRequest(BaseModel):
    """Описывает схему запроса информации об остатках на складах продавца (FBS и rFBS, API v2).

    Attributes:
        limit: Количество значений в ответе
        cursor: Указатель для выборки следующих данных
        sku: Идентификаторы товаров в системе Ozon — SKU
        offer_id: Идентификаторы товаров в системе продавца — артикулы
    """
    limit: int = Field(
        100, description="Количество значений в ответе.", ge=1
    )
    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных."
    )
    sku: Optional[list[str]] = Field(
        None, description="Идентификаторы товаров в системе Ozon — SKU."
    )
    offer_id: Optional[list[str]] = Field(
        None, description="Идентификаторы товаров в системе продавца — артикулы."
    )


class ProductInfoStocksByWarehouseFBSItem(BaseModel):
    """Данные об остатках определённого товара по схемам FBS и rFBS (API v2).

    Attributes:
        sku: Идентификатор товара в системе Ozon — SKU
        offer_id: Идентификатор товара в системе продавца — артикул
        product_id: Идентификатор товара в системе продавца
        present: Общее количество товара на складе
        reserved: Количество зарезервированных товаров
        free_stock: Количество товара, доступное к продаже
        warehouse_id: Идентификатор склада
        warehouse_name: Название склада
    """
    sku: Optional[int] = Field(None, description="Идентификатор товара в системе Ozon — SKU.")
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    product_id: Optional[int] = Field(
        None, description="Идентификатор товара в системе продавца."
    )
    present: Optional[int] = Field(None, description="Общее количество товара на складе.")
    reserved: Optional[int] = Field(
        None, description="Количество зарезервированных товаров на складе."
    )
    free_stock: Optional[int] = Field(
        None, description="Количество товара, доступное к продаже."
    )
    warehouse_id: Optional[int] = Field(None, description="Идентификатор склада.")
    warehouse_name: Optional[str] = Field(None, description="Название склада.")


class ProductInfoStocksByWarehouseFBSResponse(BaseModel):
    """Описывает схему ответа на запрос об остатках товаров по схемам FBS и rFBS (API v2).

    Attributes:
        products: Массив данных об остатках товаров по схемам FBS и rFBS
        cursor: Указатель для выборки следующих данных
        has_next: Признак, что в ответе вернулась только часть значений
    """
    products: list[ProductInfoStocksByWarehouseFBSItem] = Field(
        default_factory=list, description="Массив данных об остатках товаров по схемам FBS и rFBS."
    )
    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных."
    )
    has_next: Optional[bool] = Field(
        None, description="Признак, что в ответе вернулась только часть значений."
    )
