"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificationList"""
from typing import Optional

from pydantic import BaseModel, Field


class ProductCertificationListV1Request(BaseModel):
    """Описывает схему запроса на получение списка сертифицируемых категорий (v1).

    Attributes:
        page: Номер страницы
        page_size: Количество элементов на странице
    """
    page: Optional[int] = Field(
        None, description="Номер страницы, возвращаемой в запросе."
    )
    page_size: Optional[int] = Field(
        None, description="Количество элементов на странице."
    )


class ProductCertificationListV1Item(BaseModel):
    """Сертифицируемая категория (v1).

    Attributes:
        category_name: Название сертифицируемой категории
        is_required: Признак обязательной характеристики
    """
    category_name: Optional[str] = Field(
        None, description="Название сертифицируемой категории."
    )
    is_required: Optional[bool] = Field(
        None, description="Признак обязательной характеристики."
    )


class ProductCertificationListV1Result(BaseModel):
    """Результат запроса списка сертифицируемых категорий (v1).

    Attributes:
        certification: Информация о сертифицируемых категориях
        total: Всего категорий
    """
    certification: Optional[list[ProductCertificationListV1Item]] = Field(
        None, description="Информация о сертифицируемых категориях."
    )
    total: Optional[int] = Field(
        None, description="Всего категорий."
    )


class ProductCertificationListV1Response(BaseModel):
    """Описывает схему ответа на запрос списка сертифицируемых категорий (v1).

    Attributes:
        result: Результат запроса
    """
    result: Optional[ProductCertificationListV1Result] = Field(
        None, description="Результат запроса."
    )
