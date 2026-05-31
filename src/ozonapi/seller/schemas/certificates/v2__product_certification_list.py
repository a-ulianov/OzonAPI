"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificationListV2"""
from typing import Optional

from pydantic import BaseModel, Field


class ProductCertificationListRequest(BaseModel):
    """Описывает схему запроса на получение списка сертифицируемых категорий (v2).

    Attributes:
        page: Номер страницы
        page_size: Количество элементов на странице
    """
    page: int = Field(
        ..., description="Номер страницы."
    )
    page_size: int = Field(
        ..., description="Количество элементов на странице."
    )


class ProductCertificationListItem(BaseModel):
    """Сертифицируемая категория.

    Attributes:
        category_id: Идентификатор сертифицируемой категории
        category_name: Название сертифицируемой категории
        type_id: Идентификатор типа сертифицируемой категории
        type_name: Название типа сертифицируемой категории
        is_required: Признак обязательной характеристики
    """
    category_id: Optional[int] = Field(
        None, description="Идентификатор сертифицируемой категории."
    )
    category_name: Optional[str] = Field(
        None, description="Название сертифицируемой категории."
    )
    type_id: Optional[int] = Field(
        None, description="Идентификатор типа сертифицируемой категории."
    )
    type_name: Optional[str] = Field(
        None, description="Название типа сертифицируемой категории."
    )
    is_required: Optional[bool] = Field(
        None, description="Признак обязательной характеристики."
    )


class ProductCertificationListResponse(BaseModel):
    """Описывает схему ответа на запрос списка сертифицируемых категорий (v2).

    Attributes:
        certification: Информация о сертифицируемых категориях
        total: Всего категорий
    """
    certification: Optional[list[ProductCertificationListItem]] = Field(
        None, description="Информация о сертифицируемых категориях."
    )
    total: Optional[int] = Field(
        None, description="Всего категорий."
    )
