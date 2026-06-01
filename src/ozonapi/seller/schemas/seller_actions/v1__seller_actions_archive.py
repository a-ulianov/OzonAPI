"""https://docs.ozon.ru/api/seller/#operation/SellerActionsArchive"""
from pydantic import BaseModel, Field


class SellerActionsArchiveRequest(BaseModel):
    """Схема запроса на перенос акции в архив.

    Attributes:
        action_id: Идентификатор акции
    """

    action_id: int = Field(
        ..., description="Идентификатор акции."
    )


class SellerActionsArchiveResponse(BaseModel):
    """Схема ответа на перенос акции в архив.

    Notes:
        • Тело ответа отсутствует — успех подтверждается кодом 200.
    """
