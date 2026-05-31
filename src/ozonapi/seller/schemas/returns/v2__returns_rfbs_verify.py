"""https://docs.ozon.ru/api/seller/#operation/ReturnsAPI_ReturnsRfbsVerifyV2"""
from typing import Optional

from pydantic import BaseModel, Field


class ReturnsRfbsVerifyRequest(BaseModel):
    """Описывает схему запроса на одобрение заявки на возврат rFBS.

    Attributes:
        return_id: Идентификатор заявки на возврат
        return_method_description: Способ возврата товара
    """
    return_id: int = Field(
        ..., description="Идентификатор заявки на возврат."
    )
    return_method_description: Optional[str] = Field(
        None, description="Способ возврата товара."
    )


class ReturnsRfbsVerifyResponse(BaseModel):
    """Описывает схему ответа на запрос одобрения заявки на возврат rFBS.

    Notes:
        • При успешном выполнении API возвращает пустой объект.
    """
    pass
