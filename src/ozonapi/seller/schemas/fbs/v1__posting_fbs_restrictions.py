"""https://docs.ozon.ru/api/seller/?#operation/PostingAPI_GetRestrictions"""
from typing import Optional

from pydantic import BaseModel, Field


class PostingFBSRestrictionsRequest(BaseModel):
    """Описывает схему запроса для получения габаритных, весовых и прочих ограничений пункта приёма по номеру отправления.

    Attributes:
          posting_number: Номер отправления, для которого нужно определить ограничения
    """
    posting_number: str = Field(
        ..., description="Номер отправления, для которого нужно определить ограничения."
    )

class PostingFBSRestrictionsResponse(BaseModel):
    """Описывает схему ответа на запрос о получении габаритных, весовых и прочих ограничений пункта приёма по номеру отправления.

    Attributes:
          posting_number: Номер отправления
          max_posting_weight: Ограничение по максимальному весу в граммах
          min_posting_weight: Ограничение по минимальному весу в граммах
          width: Ограничение по ширине в сантиметрах
          length: Ограничение по длине в сантиметрах
          height: Ограничение по высоте в сантиметрах
          max_posting_price: Ограничение по максимальной стоимости отправления в рублях
          min_posting_price: Ограничение по минимальной стоимости отправления в рублях
    """
    posting_number: str = Field(
        ..., description="Номер отправления."
    )
    max_posting_weight: Optional[int] = Field(
        None, description="Ограничение по максимальному весу в граммах."
    )
    min_posting_weight: Optional[int] = Field(
        None, description="Ограничение по минимальному весу в граммах."
    )
    width: Optional[int] = Field(
        None, description="Ограничение по ширине в сантиметрах."
    )
    length: Optional[int] = Field(
        None, description="Ограничение по длине в сантиметрах."
    )
    height: Optional[int] = Field(
        None, description="Ограничение по высоте в сантиметрах."
    )
    max_posting_price: Optional[float] = Field(
        None, description="Ограничение по максимальной стоимости отправления в рублях."
    )
    min_posting_price: Optional[float] = Field(
        None, description="Ограничение по минимальной стоимости отправления в рублях."
    )