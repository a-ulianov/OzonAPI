"""https://docs.ozon.ru/api/seller/#operation/GiveoutAPI_GiveoutIsEnabled"""
from typing import Optional

from pydantic import BaseModel, Field


class ReturnGiveoutIsEnabledResponse(BaseModel):
    """Описывает схему ответа на запрос проверки возможности получения возвратных отгрузок.

    Attributes:
        enabled: Признак возможности получить возвратную отгрузку по штрихкоду
    """
    enabled: Optional[bool] = Field(
        None, description="`true`, если вы можете получить возвратную отгрузку по штрихкоду."
    )
