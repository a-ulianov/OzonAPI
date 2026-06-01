"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPDraft_FbpDraftPickUpRegistrate"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import FbpBundleItemError


class FbpDraftPickUpRegistrateRequest(BaseModel):
    """Схема запроса перевода pick-up черновика в действующую поставку.

    Attributes:
        supply_id: Идентификатор поставки
        row_version: Версия записи
    """

    supply_id: str = Field(..., description="Идентификатор поставки.")
    row_version: int = Field(..., description="Версия записи.")


class FbpDraftPickUpRegistrateError(BaseModel):
    """Ошибка регистрации pick-up поставки FBP.

    Attributes:
        order_error: Код ошибки заявки (`PICK_UP_DETAILS_IS_EMPTY`,
            `INVALID_PICK_UP_DETAILS`, `INVALID_PICK_UP_DATE`, `DRAFT_LOCKED`,
            `WAS_CANCELLED`, `INTERNAL_ERROR` и др.)
        bundle_errors: Ошибки товаров в наборе
    """

    order_error: Optional[str] = Field(
        None,
        description="Код ошибки заявки на поставку (набор открытый — тип `str`)."
    )
    bundle_errors: list[FbpBundleItemError] = Field(
        default_factory=list, description="Ошибки товаров в наборе."
    )


class FbpDraftPickUpRegistrateResponse(BaseModel):
    """Схема ответа перевода pick-up черновика в действующую поставку.

    Attributes:
        is_error: Признак наличия ошибки
        error: Ошибка регистрации поставки
        row_version: Версия записи
    """

    is_error: Optional[bool] = Field(
        None, description="Признак наличия ошибки."
    )
    error: Optional[FbpDraftPickUpRegistrateError] = Field(
        None, description="Ошибка регистрации поставки."
    )
    row_version: Optional[int] = Field(
        None, description="Версия записи."
    )
