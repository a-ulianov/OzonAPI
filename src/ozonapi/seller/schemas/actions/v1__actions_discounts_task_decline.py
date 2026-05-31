"""https://docs.ozon.ru/api/seller/#operation/DiscountTask_Decline"""
from typing import Optional

from pydantic import BaseModel, Field


class ActionsDiscountsTaskDeclineTask(BaseModel):
    """Заявка на скидку для отклонения.

    Attributes:
        id: Идентификатор заявки
        seller_comment: Комментарий продавца
    """

    id: int = Field(
        ..., description="Идентификатор заявки."
    )
    seller_comment: Optional[str] = Field(
        None, description="Комментарий продавца."
    )


class ActionsDiscountsTaskDeclineRequest(BaseModel):
    """Схема запроса на отклонение заявок на скидку.

    Attributes:
        tasks: Список заявок для отклонения
    """

    tasks: list[ActionsDiscountsTaskDeclineTask] = Field(
        ..., description="Список заявок для отклонения.",
        min_length=1
    )
