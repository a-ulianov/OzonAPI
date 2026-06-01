"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPDraft_FbpDraftDirectCreate"""
from pydantic import BaseModel, Field

from .base import FbpDraftCreateResult


class FbpDraftDirectCreateDeliveryDetails(BaseModel):
    """Детали доставки при создании черновика без указания способа доставки.

    Attributes:
        timeslot_start: Список начал желаемых таймслотов поставки
    """

    timeslot_start: list[str] = Field(
        default_factory=list,
        description="Список начал желаемых таймслотов поставки в формате RFC3339."
    )


class FbpDraftDirectCreateRequest(BaseModel):
    """Схема запроса создания черновика поставки без указания способа доставки.

    Attributes:
        bundle_id: Идентификатор набора товаров
        delivery_details: Детали доставки
        package_units_count: Количество грузовых единиц
        warehouse_id: Идентификатор склада
    """

    bundle_id: str = Field(
        ..., description="Идентификатор набора товаров."
    )
    delivery_details: FbpDraftDirectCreateDeliveryDetails = Field(
        ..., description="Детали доставки."
    )
    package_units_count: int = Field(
        ..., description="Количество грузовых единиц."
    )
    warehouse_id: int = Field(
        ..., description="Идентификатор склада."
    )


class FbpDraftDirectCreateResponse(FbpDraftCreateResult):
    """Схема ответа создания черновика поставки без указания способа доставки.

    Notes:
        • Содержит идентификаторы созданного черновика и поставки, а также версию записи.
    """
