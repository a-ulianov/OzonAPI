"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPSupply_FbpCreateAct"""
from typing import Optional

from pydantic import BaseModel, Field


class FbpActFromCreateRequest(BaseModel):
    """Схема запроса генерации акта приёмки.

    Attributes:
        supply_id: Идентификатор поставки
    """

    supply_id: str = Field(..., description="Идентификатор поставки.")


class FbpActFromCreateResponse(BaseModel):
    """Схема ответа генерации акта приёмки.

    Attributes:
        is_success: Признак успешного запуска генерации
        file_uuid: Идентификатор файла акта (для `fbp_act_from_get()`)
        errors: Ошибки запуска генерации (`INVALID_ORDER_TYPE`)
    """

    is_success: Optional[bool] = Field(
        None, description="Признак успешного запуска генерации."
    )
    file_uuid: Optional[str] = Field(
        None, description="Идентификатор файла акта (для `fbp_act_from_get()`)."
    )
    errors: list[str] = Field(
        default_factory=list,
        description="Ошибки запуска генерации (набор открытый — тип `str`)."
    )
