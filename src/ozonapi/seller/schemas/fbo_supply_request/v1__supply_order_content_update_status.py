"""Схемы метода supply_order_content_update_status (статус редактирования, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class SupplyOrderContentUpdateStatusRequest(BaseModel):
    """Параметры запроса статуса редактирования товарного состава.

    Attributes:
        operation_id: Идентификатор операции редактирования
    """
    operation_id: str = Field(
        ..., description="Идентификатор операции редактирования."
    )


class SupplyOrderContentUpdateStatusResponse(BaseModel):
    """Ответ со статусом редактирования товарного состава.

    Attributes:
        errors: Ошибки редактирования
        new_bundle_id: Идентификатор нового товарного состава
        status: Статус операции редактирования
    """
    errors: Optional[list[str]] = Field(
        None, description="Ошибки редактирования."
    )
    new_bundle_id: Optional[str] = Field(
        None, description="Идентификатор нового товарного состава."
    )
    status: Optional[str] = Field(
        None, description="Статус операции редактирования."
    )
