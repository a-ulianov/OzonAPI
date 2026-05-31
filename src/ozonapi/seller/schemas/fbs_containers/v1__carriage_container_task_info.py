"""https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageContainerTaskInfo"""
from typing import Optional

from pydantic import BaseModel, Field


class CarriageContainerTaskInfoRequest(BaseModel):
    """Описывает схему запроса на получение статуса задачи грузового места.

    Attributes:
        task_id: Идентификатор задачи
    """
    task_id: int = Field(
        ..., description="Идентификатор задачи (возвращается методами наполнения/подтверждения грузомест)."
    )


class CarriageContainerTaskInfoResponse(BaseModel):
    """Описывает схему ответа на запрос статуса задачи грузового места.

    Attributes:
        status: Статус выполнения задачи (`pending`, `success`, `error` и т.д.)
        error_message: Текст ошибки
    """
    status: Optional[str] = Field(
        None, description="Статус выполнения задачи: `pending` — в обработке, `success` — выполнена, `error` — ошибка."
    )
    error_message: Optional[str] = Field(
        None, description="Текст ошибки."
    )
