"""https://docs.ozon.ru/api/seller/#operation/SellerActionsChangeActivity"""
from pydantic import BaseModel, Field


class SellerActionsChangeActivityRequest(BaseModel):
    """Схема запроса на включение или выключение акции.

    Attributes:
        action_id: Идентификатор акции
        is_turn_on: Включить акцию (`true`) или выключить (`false`)
    """

    action_id: int = Field(
        ..., description="Идентификатор акции."
    )
    is_turn_on: bool = Field(
        ..., description="Включить акцию (`true`) или выключить (`false`)."
    )


class SellerActionsChangeActivityResponse(BaseModel):
    """Схема ответа на включение или выключение акции.

    Notes:
        • Тело ответа отсутствует — успех подтверждается кодом 200.
    """
