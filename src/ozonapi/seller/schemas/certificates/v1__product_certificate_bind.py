"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificateBind"""
from typing import Optional

from pydantic import BaseModel, Field


class ProductCertificateBindRequest(BaseModel):
    """Описывает схему запроса на привязку сертификата к товару.

    Attributes:
        certificate_id: Идентификатор сертификата
        product_id: Массив идентификаторов товаров
    """
    certificate_id: int = Field(
        ..., description="Идентификатор сертификата, который нужно привязать."
    )
    product_id: list[int] = Field(
        ..., description="Массив идентификаторов товаров, к которым привязывается сертификат."
    )


class ProductCertificateBindResponse(BaseModel):
    """Описывает схему ответа на запрос привязки сертификата к товару.

    Attributes:
        result: Результат обработки запроса (`true`, если выполнено успешно)
    """
    result: Optional[bool] = Field(
        None, description="Результат обработки запроса. `true`, если выполнено успешно."
    )
