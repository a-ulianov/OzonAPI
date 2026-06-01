"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPDraft_FbpDraftPickUpProductValidate"""
from typing import Optional

from pydantic import BaseModel, Field

from .v1__fbp_draft_direct_product_validate import (
    FbpProductValidateApprovedItem,
    FbpProductValidateRejectedItem,
    FbpProductValidateSkuItem,
)


class FbpDraftPickUpProductValidateRequest(BaseModel):
    """Схема запроса проверки списка товаров для pick-up поставки.

    Attributes:
        skus: Список товаров для проверки
        warehouse_id: Идентификатор склада
    """

    skus: list[FbpProductValidateSkuItem] = Field(
        default_factory=list, description="Список товаров для проверки."
    )
    warehouse_id: int = Field(..., description="Идентификатор склада.")


class FbpDraftPickUpProductValidateResponse(BaseModel):
    """Схема ответа проверки списка товаров для pick-up поставки.

    Attributes:
        bundle_generated: Признак того, что набор товаров сформирован
        bundle_id: Идентификатор сформированного набора
        approved_items: Принятые товары
        rejected_items: Отклонённые товары
    """

    bundle_generated: Optional[bool] = Field(
        None, description="Признак того, что набор товаров сформирован."
    )
    bundle_id: Optional[str] = Field(
        None, description="Идентификатор сформированного набора товаров."
    )
    approved_items: list[FbpProductValidateApprovedItem] = Field(
        default_factory=list, description="Принятые товары."
    )
    rejected_items: list[FbpProductValidateRejectedItem] = Field(
        default_factory=list, description="Отклонённые товары."
    )
