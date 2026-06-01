"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPDraft_FbpDraftDropOffProvinceList"""
from typing import Optional

from pydantic import BaseModel, Field


class FbpDraftDropOffProvinceListRequest(BaseModel):
    """Схема запроса списка провинций для drop-off поставки.

    Attributes:
        warehouse_id: Идентификатор склада
    """

    warehouse_id: int = Field(..., description="Идентификатор склада.")


class FbpDropOffProvince(BaseModel):
    """Провинция для drop-off поставки.

    Attributes:
        province_uuid: Идентификатор провинции
        name: Название провинции
        points_count: Количество drop-off пунктов в провинции
    """

    province_uuid: Optional[str] = Field(None, description="Идентификатор провинции.")
    name: Optional[str] = Field(None, description="Название провинции.")
    points_count: Optional[int] = Field(
        None, description="Количество drop-off пунктов в провинции."
    )


class FbpDraftDropOffProvinceListResponse(BaseModel):
    """Схема ответа со списком провинций для drop-off поставки.

    Attributes:
        provinces: Список провинций
    """

    provinces: list[FbpDropOffProvince] = Field(
        default_factory=list, description="Список провинций."
    )
