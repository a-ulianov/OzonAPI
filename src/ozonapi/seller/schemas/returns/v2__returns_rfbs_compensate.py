"""https://docs.ozon.ru/api/seller/#operation/ReturnsAPI_ReturnsRfbsCompensateV2"""
from typing import Optional

from pydantic import BaseModel, Field


class ReturnsRfbsCompensateRequest(BaseModel):
    """Описывает схему запроса на возврат части стоимости товара rFBS.

    Attributes:
        return_id: Идентификатор заявки на возврат
        compensation_amount: Сумма компенсации
    """
    return_id: int = Field(
        ..., description="Идентификатор заявки на возврат."
    )
    compensation_amount: Optional[str] = Field(
        None, description="Сумма компенсации."
    )


class ReturnsRfbsCompensateResponse(BaseModel):
    """Описывает схему ответа на запрос возврата части стоимости товара rFBS.

    Notes:
        • При успешном выполнении API возвращает пустой объект.
    """
    pass
