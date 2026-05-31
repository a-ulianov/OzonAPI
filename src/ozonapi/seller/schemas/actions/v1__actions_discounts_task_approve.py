"""https://docs.ozon.ru/api/seller/#operation/DiscountTask_Approve"""
from typing import Optional

from pydantic import BaseModel, Field


class ActionsDiscountsTaskApproveTask(BaseModel):
    """Заявка на скидку для согласования.

    Attributes:
        id: Идентификатор заявки
        approved_price: Согласованная цена
        seller_comment: Комментарий продавца
        approved_quantity_min: Минимальное согласованное количество
        approved_quantity_max: Максимальное согласованное количество
    """

    id: int = Field(
        ..., description="Идентификатор заявки."
    )
    approved_price: float = Field(
        ..., description="Согласованная цена."
    )
    seller_comment: Optional[str] = Field(
        None, description="Комментарий продавца."
    )
    approved_quantity_min: Optional[int] = Field(
        None, description="Минимальное согласованное количество."
    )
    approved_quantity_max: Optional[int] = Field(
        None, description="Максимальное согласованное количество."
    )


class ActionsDiscountsTaskApproveRequest(BaseModel):
    """Схема запроса на согласование заявок на скидку.

    Attributes:
        tasks: Список заявок для согласования
    """

    tasks: list[ActionsDiscountsTaskApproveTask] = Field(
        ..., description="Список заявок для согласования.",
        min_length=1
    )
