"""Схемы метода product_quant_list (список эконом-товаров, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.products import Visibility


class ProductQuantListRequest(BaseModel):
    """Параметры запроса списка эконом-товаров.

    Attributes:
        cursor: Указатель для выборки следующих данных
        limit: Количество значений в ответе
        visibility: Фильтр по видимости товаров
    """
    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных."
    )
    limit: Optional[int] = Field(None, description="Количество значений в ответе.")
    visibility: Optional[Visibility] = Field(
        None, description="Фильтр по видимости товаров."
    )


class ProductQuantListProductQuant(BaseModel):
    """Квант товара.

    Attributes:
        quant_code: Идентификатор кванта
        quant_size: Размер кванта
    """
    quant_code: Optional[str] = Field(None, description="Идентификатор кванта.")
    quant_size: Optional[int] = Field(None, description="Размер кванта.")


class ProductQuantListProduct(BaseModel):
    """Эконом-товар.

    Attributes:
        offer_id: Идентификатор товара в системе продавца — артикул
        product_id: Идентификатор товара в системе Ozon — product_id
        quants: Список квантов товара
    """
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    product_id: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — product_id."
    )
    quants: list[ProductQuantListProductQuant] = Field(
        default_factory=list, description="Список квантов товара."
    )


class ProductQuantListResponse(BaseModel):
    """Ответ со списком эконом-товаров.

    Attributes:
        cursor: Указатель для выборки следующих данных
        products: Эконом-товары
        total_items: Остаток на всех складах, шт.
    """
    cursor: str = Field("", description="Указатель для выборки следующих данных.")
    products: list[ProductQuantListProduct] = Field(
        default_factory=list, description="Эконом-товары."
    )
    total_items: int = Field(0, description="Остаток на всех складах, шт.")
