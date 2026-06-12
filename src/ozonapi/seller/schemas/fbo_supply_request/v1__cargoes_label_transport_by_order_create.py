"""Схемы метода cargoes_label_transport_by_order_create (этикетки транспортных грузомест по поставке, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class CargoesLabelTransportByOrderCreateRequest(BaseModel):
    """Параметры запроса генерации этикеток транспортных грузомест по поставке.

    Attributes:
        order_id: Идентификатор поставки
    """
    order_id: int = Field(..., description="Идентификатор поставки.")


class CargoesLabelTransportByOrderCreateResponse(BaseModel):
    """Ответ на генерацию этикеток транспортных грузомест по поставке.

    Attributes:
        error_reasons: Причины ошибок
        operation_id: Идентификатор операции
    """
    error_reasons: Optional[list[str]] = Field(
        None, description="Причины ошибок."
    )
    operation_id: Optional[str] = Field(
        None, description="Идентификатор операции."
    )
