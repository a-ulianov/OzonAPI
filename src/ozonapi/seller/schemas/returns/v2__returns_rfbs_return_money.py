"""https://docs.ozon.ru/api/seller/#operation/ReturnsAPI_ReturnsRfbsReturnMoneyV2"""
from typing import Optional

from pydantic import BaseModel, Field


class ReturnsRfbsReturnMoneyRequest(BaseModel):
    """Описывает схему запроса на возврат денег покупателю rFBS.

    Attributes:
        return_id: Идентификатор заявки на возврат
        return_for_back_way: Сумма, возмещаемая покупателю за пересылку
    """
    return_id: int = Field(
        ..., description="Идентификатор заявки на возврат."
    )
    return_for_back_way: Optional[int] = Field(
        None, description="Сумма, возмещаемая покупателю за пересылку."
    )


class ReturnsRfbsReturnMoneyResponse(BaseModel):
    """Описывает схему ответа на запрос возврата денег покупателю rFBS.

    Notes:
        • При успешном выполнении API возвращает пустой объект.
    """
    pass
