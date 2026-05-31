"""https://docs.ozon.ru/api/seller/#operation/AssemblyAPI_AssemblyFbsProductList"""
from typing import Optional

from pydantic import BaseModel, Field


class AssemblyFbsProductListFilter(BaseModel):
    """Фильтр для получения списка товаров в отправлениях.

    Attributes:
        delivery_method_id: Идентификатор способа доставки
        cutoff_from: Начало периода времени сборки заказа
        cutoff_to: Конец периода времени сборки заказа
    """
    delivery_method_id: Optional[int] = Field(
        None, description="Идентификатор способа доставки."
    )
    cutoff_from: Optional[str] = Field(
        None, description="Начало периода времени, до которого продавцу нужно собрать заказ."
    )
    cutoff_to: Optional[str] = Field(
        None, description="Конец периода времени, до которого продавцу нужно собрать заказ."
    )


class AssemblyFbsProductListRequest(BaseModel):
    """Описывает схему запроса на получение списка товаров в отправлениях.

    Attributes:
        filter: Фильтр для поиска товаров
        limit: Количество значений на странице
        offset: Количество элементов, которое будет пропущено в ответе
        sort_dir: Направление сортировки (`ASC` или `DESC`)
    """
    filter: AssemblyFbsProductListFilter = Field(
        ..., description="Фильтр для поиска товаров."
    )
    limit: int = Field(
        ..., description="Количество значений на странице."
    )
    offset: Optional[int] = Field(
        None, description="Количество элементов, которое будет пропущено в ответе."
    )
    sort_dir: Optional[str] = Field(
        None, description="Направление сортировки: `ASC` — по возрастанию, `DESC` — по убыванию."
    )


class AssemblyFbsProductListPosting(BaseModel):
    """Отправление, в котором находится товар.

    Attributes:
        posting_number: Номер отправления
        quantity: Количество товаров в отправлении
    """
    posting_number: Optional[str] = Field(
        None, description="Номер отправления."
    )
    quantity: Optional[int] = Field(
        None, description="Количество товаров в отправлении."
    )


class AssemblyFbsProductListProduct(BaseModel):
    """Товар в отправлениях.

    Attributes:
        offer_id: Идентификатор товара в системе продавца — артикул
        product_name: Название товара
        quantity: Количество товара
        sku: Идентификатор товара в системе Ozon — SKU
        picture_url: Ссылка на изображение товара
        postings: Список отправлений
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
    postings: Optional[list[AssemblyFbsProductListPosting]] = Field(
        None, description="Список отправлений."
    )


class AssemblyFbsProductListResponse(BaseModel):
    """Описывает схему ответа на запрос списка товаров в отправлениях.

    Attributes:
        products: Список товаров
        products_count: Количество товаров
        has_next: Признак наличия следующей страницы
    """
    products: Optional[list[AssemblyFbsProductListProduct]] = Field(
        None, description="Список товаров."
    )
    products_count: Optional[int] = Field(
        None, description="Количество товаров."
    )
    has_next: Optional[bool] = Field(
        None, description="`true`, если в ответе вернули не все товары."
    )
