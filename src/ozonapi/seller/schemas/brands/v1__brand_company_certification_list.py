"""https://docs.ozon.ru/api/seller/#operation/BrandAPI_BrandCompanyCertificationList"""
from typing import Optional

from pydantic import BaseModel, Field


class BrandCompanyCertificationListRequest(BaseModel):
    """Схема запроса списка сертифицируемых брендов.

    Attributes:
        page: Номер страницы, возвращаемой в ответе
        page_size: Количество элементов на странице
    """

    page: Optional[int] = Field(
        None, description="Номер страницы, возвращаемой в ответе."
    )
    page_size: Optional[int] = Field(
        None, description="Количество элементов на странице."
    )


class BrandCertification(BaseModel):
    """Бренд и признак необходимости сертификата.

    Attributes:
        brand_name: Название бренда
        has_certificate: Признак того, что для бренда нужен сертификат
    """

    brand_name: Optional[str] = Field(
        None, description="Название бренда."
    )
    has_certificate: Optional[bool] = Field(
        None, description="Признак того, что для бренда необходим сертификат."
    )


class BrandCompanyCertificationListResult(BaseModel):
    """Результат запроса списка сертифицируемых брендов.

    Attributes:
        brand_certification: Список брендов с признаком необходимости сертификата
        total: Общее количество брендов
    """

    brand_certification: list[BrandCertification] = Field(
        default_factory=list,
        description="Список брендов с признаком необходимости сертификата."
    )
    total: Optional[int] = Field(
        None, description="Общее количество брендов."
    )


class BrandCompanyCertificationListResponse(BaseModel):
    """Схема ответа со списком сертифицируемых брендов.

    Attributes:
        result: Результат запроса со списком брендов и их общим количеством
    """

    result: BrandCompanyCertificationListResult = Field(
        default_factory=BrandCompanyCertificationListResult,
        description="Результат запроса со списком брендов и их общим количеством."
    )
