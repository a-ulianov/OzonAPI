"""https://docs.ozon.ru/api/seller/#operation/ReturnsAPI_ReturnsRfbsActionSet"""
from typing import Optional

from pydantic import BaseModel, Field


class ReturnsRfbsActionSetRequest(BaseModel):
    """Описывает схему запроса на передачу доступных действий для rFBS возвратов.

    Attributes:
        return_id: Идентификатор заявки на возврат
        id: Идентификатор действия
        comment: Комментарий продавца
        compensation_amount: Сумма компенсации
        rejection_reason_id: Идентификатор причины отмены
        return_for_back_way: Сумма, возмещаемая покупателю за пересылку
    """
    return_id: int = Field(
        ..., description="Идентификатор заявки на возврат."
    )
    id: Optional[int] = Field(
        None, description="Идентификатор действия."
    )
    comment: Optional[str] = Field(
        None, description="Комментарий продавца. Обязателен для некоторых действий."
    )
    compensation_amount: Optional[float] = Field(
        None, description="Сумма компенсации. Обязательна для действия компенсации."
    )
    rejection_reason_id: Optional[int] = Field(
        None, description="Идентификатор причины отмены. Обязателен для действия отклонения."
    )
    return_for_back_way: Optional[float] = Field(
        None, description="Сумма, возмещаемая покупателю за пересылку."
    )


class ReturnsRfbsActionSetResponse(BaseModel):
    """Описывает схему ответа на запрос передачи доступных действий для rFBS возвратов.

    Notes:
        • При успешном выполнении API возвращает пустой объект.
    """
    pass
