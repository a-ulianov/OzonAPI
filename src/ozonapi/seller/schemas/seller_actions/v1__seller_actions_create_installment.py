"""https://docs.ozon.ru/api/seller/#operation/SellerActionsCreateInstallment"""
from pydantic import BaseModel, Field


class SellerActionsCreateInstallmentRequest(BaseModel):
    """Схема запроса на создание акции с механикой «Беспроцентная рассрочка».

    Attributes:
        date_start: Дата и время начала акции
        title: Название акции
    """

    date_start: str = Field(
        ..., description="Дата и время начала акции в формате RFC3339."
    )
    title: str = Field(
        ..., description="Название акции."
    )


class SellerActionsCreateInstallmentResponse(BaseModel):
    """Схема ответа на создание акции с механикой «Беспроцентная рассрочка».

    Attributes:
        action_id: Идентификатор созданной акции
    """

    action_id: int = Field(
        ..., description="Идентификатор созданной акции."
    )
