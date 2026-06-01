"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPDraft_FbpDraftDropOffPointList"""
from typing import Optional

from pydantic import BaseModel, Field


class FbpDraftDropOffPointListRequest(BaseModel):
    """Схема запроса списка drop-off пунктов в провинции.

    Attributes:
        warehouse_id: Идентификатор склада
        province_uuid: Идентификатор провинции
        page_size: Количество элементов на странице
        next_page_number: Номер следующей страницы (пагинация)
    """

    warehouse_id: int = Field(..., description="Идентификатор склада.")
    province_uuid: str = Field(..., description="Идентификатор провинции.")
    page_size: int = Field(..., description="Количество элементов на странице.")
    next_page_number: Optional[int] = Field(
        None, description="Номер следующей страницы (для постраничной выборки)."
    )


class FbpDropOffPoint(BaseModel):
    """Drop-off пункт.

    Attributes:
        drop_off_point_id: Идентификатор drop-off пункта
        province_uuid: Идентификатор провинции
        city: Город
        point_address: Адрес пункта
        nearest_drop_off_date: Ближайшая дата сдачи
    """

    drop_off_point_id: Optional[int] = Field(
        None, description="Идентификатор drop-off пункта."
    )
    province_uuid: Optional[str] = Field(None, description="Идентификатор провинции.")
    city: Optional[str] = Field(None, description="Город.")
    point_address: Optional[str] = Field(None, description="Адрес пункта.")
    nearest_drop_off_date: Optional[str] = Field(
        None, description="Ближайшая дата сдачи в формате RFC3339."
    )


class FbpDraftDropOffPointListResponse(BaseModel):
    """Схема ответа со списком drop-off пунктов в провинции.

    Attributes:
        drop_off_points: Список drop-off пунктов
    """

    drop_off_points: list[FbpDropOffPoint] = Field(
        default_factory=list, description="Список drop-off пунктов."
    )
