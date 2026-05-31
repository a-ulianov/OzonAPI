"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificateUnbind"""
from typing import Optional

from pydantic import BaseModel, Field


class ProductCertificateUnbindRequest(BaseModel):
    """Описывает схему запроса на отвязку товара от сертификата.

    Attributes:
        certificate_id: Идентификатор сертификата
        product_id: Список идентификаторов товаров
    """
    certificate_id: int = Field(
        ..., description="Идентификатор сертификата."
    )
    product_id: list[str] = Field(
        ..., description="Список идентификаторов товаров, которые нужно отвязать."
    )


class ProductCertificateUnbindItem(BaseModel):
    """Результат отвязки товара от сертификата.

    Attributes:
        product_id: Идентификатор товара в системе Ozon
        updated: Был ли товар отвязан от сертификата
        error: Сообщение об ошибке при отвязывании
    """
    product_id: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon."
    )
    updated: Optional[bool] = Field(
        None, description="Был ли товар отвязан от сертификата."
    )
    error: Optional[str] = Field(
        None, description="Сообщение об ошибке при отвязывании."
    )


class ProductCertificateUnbindResponse(BaseModel):
    """Описывает схему ответа на запрос отвязки товара от сертификата.

    Attributes:
        result: Результат работы метода
    """
    result: Optional[list[ProductCertificateUnbindItem]] = Field(
        None, description="Результат работы метода."
    )
