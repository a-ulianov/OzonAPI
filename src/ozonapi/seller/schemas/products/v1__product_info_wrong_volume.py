"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductInfoWrongVolume"""
from typing import Optional

from pydantic import BaseModel, Field


class ProductInfoWrongVolumeRequest(BaseModel):
    """Схема запроса списка товаров с некорректными ОВХ.

    Attributes:
        cursor: Указатель для выборки следующих данных (курсорная пагинация)
        limit: Максимальное количество элементов в ответе (1–1000)
    """

    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных (курсорная пагинация)."
    )
    limit: Optional[int] = Field(
        None, description="Максимальное количество элементов в ответе (от 1 до 1000)."
    )


class ProductInfoWrongVolumeProduct(BaseModel):
    """Товар с некорректными объёмно-весовыми характеристиками (ОВХ).

    Attributes:
        product_id: Идентификатор товара
        sku: Идентификатор товара в системе Ozon — SKU
        offer_id: Идентификатор товара в системе продавца — артикул
        name: Название товара
        height: Высота упаковки, мм
        length: Длина упаковки, мм
        width: Ширина упаковки, мм
        weight: Вес товара в упаковке, г
    """

    product_id: Optional[int] = Field(
        None, description="Идентификатор товара."
    )
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    name: Optional[str] = Field(
        None, description="Название товара."
    )
    height: Optional[int] = Field(
        None, description="Высота упаковки, мм."
    )
    length: Optional[int] = Field(
        None, description="Длина упаковки, мм."
    )
    width: Optional[int] = Field(
        None, description="Ширина упаковки, мм."
    )
    weight: Optional[int] = Field(
        None, description="Вес товара в упаковке, г."
    )


class ProductInfoWrongVolumeResponse(BaseModel):
    """Схема ответа со списком товаров с некорректными ОВХ.

    Attributes:
        cursor: Указатель для выборки следующих данных (курсорная пагинация)
        products: Список товаров с некорректными ОВХ
    """

    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных (курсорная пагинация)."
    )
    products: list[ProductInfoWrongVolumeProduct] = Field(
        default_factory=list, description="Список товаров с некорректными ОВХ."
    )
