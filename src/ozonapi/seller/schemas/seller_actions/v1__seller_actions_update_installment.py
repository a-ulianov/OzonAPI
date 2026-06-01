"""https://docs.ozon.ru/api/seller/#operation/SellerActionsUpdateInstallment"""
from pydantic import BaseModel, Field


class SellerActionsUpdateInstallmentParameters(BaseModel):
    """Параметры обновления акции с механикой «Беспроцентная рассрочка».

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


class SellerActionsUpdateInstallmentRequest(BaseModel):
    """Схема запроса на обновление акции с механикой «Беспроцентная рассрочка».

    Attributes:
        action_id: Идентификатор акции
        action_parameters: Новые параметры акции
    """

    action_id: int = Field(
        ..., description="Идентификатор акции."
    )
    action_parameters: SellerActionsUpdateInstallmentParameters = Field(
        ..., description="Новые параметры акции."
    )


class SellerActionsUpdateInstallmentResponse(BaseModel):
    """Схема ответа на обновление акции с механикой «Беспроцентная рассрочка».

    Notes:
        • Тело ответа отсутствует — успех подтверждается кодом 200.
    """
