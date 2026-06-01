"""Схемы метода posting_fbs_package_label_create (создание задания, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class PostingFBSPackageLabelCreateV1Request(BaseModel):
    """Параметры запроса создания задания на формирование этикеток (v1).

    Attributes:
        posting_number: Номера отправлений, для которых нужны этикетки
    """
    posting_number: list[str] = Field(
        ..., description="Номера отправлений, для которых нужны этикетки."
    )


class PostingFBSPackageLabelCreateV1Result(BaseModel):
    """Результат создания задания на формирование этикеток (v1).

    Attributes:
        task_id: Идентификатор задания на формирование этикеток
    """
    task_id: Optional[int] = Field(
        None, description="Идентификатор задания на формирование этикеток."
    )


class PostingFBSPackageLabelCreateV1Response(BaseModel):
    """Ответ на создание задания на формирование этикеток (v1).

    Attributes:
        result: Результат создания задания
    """
    result: Optional[PostingFBSPackageLabelCreateV1Result] = Field(
        None, description="Результат создания задания."
    )
