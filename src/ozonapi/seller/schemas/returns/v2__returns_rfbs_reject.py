"""https://docs.ozon.ru/api/seller/#operation/ReturnsAPI_ReturnsRfbsRejectV2"""
from typing import Optional

from pydantic import BaseModel, Field


class ReturnsRfbsRejectRequest(BaseModel):
    """Описывает схему запроса на отклонение заявки на возврат rFBS.

    Attributes:
        return_id: Идентификатор заявки на возврат
        rejection_reason_id: Идентификатор причины отмены
        comment: Комментарий
    """
    return_id: int = Field(
        ..., description="Идентификатор заявки на возврат."
    )
    rejection_reason_id: int = Field(
        ..., description="Идентификатор причины отмены."
    )
    comment: Optional[str] = Field(
        None, description="Комментарий. Передайте, если он обязателен для выбранной причины."
    )


class ReturnsRfbsRejectResponse(BaseModel):
    """Описывает схему ответа на запрос отклонения заявки на возврат rFBS.

    Notes:
        • При успешном выполнении API возвращает пустой объект.
    """
    pass
