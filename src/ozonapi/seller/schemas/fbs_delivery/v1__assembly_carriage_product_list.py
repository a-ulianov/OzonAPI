"""https://docs.ozon.ru/api/seller/#operation/AssemblyAPI_AssemblyCarriageProductList"""
from typing import Optional

from pydantic import BaseModel, Field


class AssemblyCarriageProductListFilter(BaseModel):
    """Фильтр для получения списка товаров в отгрузке.

    Attributes:
        carriage_id: Идентификатор перевозки
        delivery_method_id: Идентификатор метода доставки
        cutoff_from: Начало периода времени сборки заказа
        cutoff_to: Конец периода времени сборки заказа
    """
    carriage_id: Optional[int] = Field(
        None, description="Идентификатор перевозки."
    )
    delivery_method_id: Optional[int] = Field(
        None, description="Идентификатор метода доставки."
    )
    cutoff_from: Optional[str] = Field(
        None, description="Начало периода времени, до которого продавцу нужно собрать заказ."
    )
    cutoff_to: Optional[str] = Field(
        None, description="Конец периода времени, до которого продавцу нужно собрать заказ."
    )


class AssemblyCarriageProductListRequest(BaseModel):
    """Описывает схему запроса на получение списка товаров в отгрузке.

    Attributes:
        filter: Фильтр для поиска товаров
        limit: Количество значений на странице
        cursor: Указатель для выборки следующих данных
    """
    filter: AssemblyCarriageProductListFilter = Field(
        ..., description="Фильтр для поиска товаров."
    )
    limit: int = Field(
        ..., description="Количество значений на странице."
    )
    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных."
    )


class AssemblyCarriageProductListProduct(BaseModel):
    """Товар в отгрузке.

    Attributes:
        offer_id: Идентификатор товара в системе продавца — артикул
        product_name: Название товара
        quantity: Количество товара
        sku: Идентификатор товара в системе Ozon — SKU
        picture_url: Ссылка на изображение товара
        posting_numbers: Номера отправлений
    """
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    product_name: Optional[str] = Field(
        None, description="Название товара."
    )
    quantity: Optional[int] = Field(
        None, description="Количество товара."
    )
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    picture_url: Optional[str] = Field(
        None, description="Ссылка на изображение товара."
    )
    posting_numbers: Optional[list[str]] = Field(
        None, description="Номера отправлений."
    )


class AssemblyCarriageProductListResponse(BaseModel):
    """Описывает схему ответа на запрос списка товаров в отгрузке.

    Attributes:
        products: Список товаров
        cursor: Указатель для выборки следующих данных
    """
    products: Optional[list[AssemblyCarriageProductListProduct]] = Field(
        None, description="Список товаров."
    )
    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных."
    )
