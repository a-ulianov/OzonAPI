"""Схемы метода cargoes_label_transport_status (статус этикеток транспортных грузомест, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class CargoesLabelTransportStatusRequest(BaseModel):
    """Параметры запроса статуса генерации этикеток транспортных грузомест.

    Attributes:
        operation_id: Идентификатор операции генерации этикеток
    """
    operation_id: str = Field(
        ..., description="Идентификатор операции генерации этикеток."
    )


class CargoesLabelTransportStatusResult(BaseModel):
    """Результат генерации этикеток транспортных грузомест.

    Attributes:
        file_url: Ссылка на файл с этикетками
    """
    file_url: Optional[str] = Field(
        None, description="Ссылка на файл с этикетками."
    )


class CargoesLabelTransportStatusResponse(BaseModel):
    """Ответ со статусом генерации этикеток транспортных грузомест.

    Attributes:
        error_reasons: Причины ошибок
        result: Результат генерации
        status: Статус операции (`SUCCESS`, `IN_PROGRESS`, `FAILED`)
    """
    error_reasons: Optional[list[str]] = Field(
        None, description="Причины ошибок."
    )
    result: Optional[CargoesLabelTransportStatusResult] = Field(
        None, description="Результат генерации."
    )
    status: Optional[str] = Field(
        None,
        description="Статус операции. Возможные значения: `SUCCESS`, `IN_PROGRESS`, `FAILED`."
    )
