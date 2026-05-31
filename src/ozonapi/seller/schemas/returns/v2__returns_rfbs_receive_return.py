"""https://docs.ozon.ru/api/seller/#operation/ReturnsAPI_ReturnsRfbsReceiveReturnV2"""
from pydantic import BaseModel, Field


class ReturnsRfbsReceiveReturnRequest(BaseModel):
    """Описывает схему запроса на подтверждение получения товара на проверку rFBS.

    Attributes:
        return_id: Идентификатор заявки на возврат
    """
    return_id: int = Field(
        ..., description="Идентификатор заявки на возврат."
    )


class ReturnsRfbsReceiveReturnResponse(BaseModel):
    """Описывает схему ответа на запрос подтверждения получения товара на проверку rFBS.

    Notes:
        • При успешном выполнении API возвращает пустой объект.
    """
    pass
