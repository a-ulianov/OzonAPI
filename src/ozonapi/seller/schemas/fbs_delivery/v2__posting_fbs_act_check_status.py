"""https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingFBSActCheckStatus"""
from typing import Optional

from pydantic import BaseModel, Field


class PostingFBSActCheckStatusRequest(BaseModel):
    """Описывает схему запроса на проверку статуса отгрузки и документов.

    Attributes:
        id: Номер задания на формирование документов
    """
    id: int = Field(
        ..., description="Номер задания на формирование документов (также идентификатор отгрузки)."
    )


class PostingFBSActCheckStatusResult(BaseModel):
    """Статус формирования отгрузки и документов.

    Attributes:
        act_type: Тип документов
        added_to_act: Номера отправлений, добавленных в перевозку
        removed_from_act: Номера отправлений, не попавших в перевозку
        status: Статус запроса
        is_partial: Признак частичной перевозки
        has_postings_for_next_carriage: Признак наличия отправлений для следующей перевозки
        partial_num: Порядковый номер частичной перевозки
    """
    act_type: Optional[str] = Field(
        None, description="Тип документов."
    )
    added_to_act: Optional[list[str]] = Field(
        None, description="Массив с номерами отправлений, которые добавлены в перевозку."
    )
    removed_from_act: Optional[list[str]] = Field(
        None, description="Массив с номерами отправлений, которые не попали в перевозку."
    )
    status: Optional[str] = Field(
        None, description="Статус запроса: `in_process` — документы формируются, `ready` — готовы, `error` — ошибка."
    )
    is_partial: Optional[bool] = Field(
        None, description="Признак частичной перевозки. `true`, если перевозка частичная."
    )
    has_postings_for_next_carriage: Optional[bool] = Field(
        None, description="`true`, если есть отправления, не попавшие в текущую перевозку."
    )
    partial_num: Optional[int] = Field(
        None, description="Порядковый номер частичной перевозки."
    )


class PostingFBSActCheckStatusResponse(BaseModel):
    """Описывает схему ответа на запрос статуса отгрузки и документов.

    Attributes:
        result: Статус формирования отгрузки и документов
    """
    result: Optional[PostingFBSActCheckStatusResult] = Field(
        None, description="Статус формирования отгрузки и документов."
    )
