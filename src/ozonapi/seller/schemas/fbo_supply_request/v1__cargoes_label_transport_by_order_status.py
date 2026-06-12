"""Схемы метода cargoes_label_transport_by_order_status (статус этикеток по поставке, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class CargoesLabelTransportByOrderStatusRequest(BaseModel):
    """Параметры запроса статуса генерации этикеток транспортных грузомест по поставке.

    Attributes:
        operation_id: Идентификатор операции генерации этикеток
    """
    operation_id: str = Field(
        ..., description="Идентификатор операции генерации этикеток."
    )


class CargoesLabelTransportByOrderStatusResult(BaseModel):
    """Результат генерации этикеток транспортных грузомест по поставке.

    Attributes:
        file_url: Ссылка на файл с этикетками
        skipped_supplies_ids: Идентификаторы пропущенных поставок
    """
    file_url: Optional[str] = Field(
        None, description="Ссылка на файл с этикетками."
    )
    skipped_supplies_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы пропущенных поставок."
    )


class CargoesLabelTransportByOrderStatusResponse(BaseModel):
    """Ответ со статусом генерации этикеток транспортных грузомест по поставке.

    Attributes:
        error_reasons: Причины ошибок
        result: Результат генерации
        status: Статус операции (`SUCCESS`, `IN_PROGRESS`, `FAILED`)
    """
    error_reasons: Optional[list[str]] = Field(
        None, description="Причины ошибок."
    )
    result: Optional[CargoesLabelTransportByOrderStatusResult] = Field(
        None, description="Результат генерации."
    )
    status: Optional[str] = Field(
        None,
        description="Статус операции. Возможные значения: `SUCCESS`, `IN_PROGRESS`, `FAILED`."
    )
