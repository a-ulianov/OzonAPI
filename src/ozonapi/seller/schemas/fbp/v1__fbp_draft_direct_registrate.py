"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPDraft_FbpDraftDirectRegistrate"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import FbpBundleItemError


class FbpDraftDirectRegistrateRequest(BaseModel):
    """Схема запроса перевода черновика в действующую поставку.

    Attributes:
        supply_id: Идентификатор поставки
        row_version: Версия записи
    """

    supply_id: str = Field(..., description="Идентификатор поставки.")
    row_version: int = Field(..., description="Версия записи.")


class FbpDraftDirectRegistrateError(BaseModel):
    """Ошибка регистрации поставки FBP.

    Attributes:
        order_error: Код ошибки заявки (`INVALID_NUMBER_OF_PACKAGE_UNITS`,
            `MAXIMUM_NUMBER_OF_UNIQUE_SKU_REACHED`, `INVALID_TIMESLOT`,
            `DRAFT_LOCKED`, `WAS_CANCELLED`, `INTERNAL_ERROR` и др.)
        bundle_errors: Ошибки товаров в наборе
    """

    order_error: Optional[str] = Field(
        None,
        description="Код ошибки заявки на поставку (набор открытый — тип `str`)."
    )
    bundle_errors: list[FbpBundleItemError] = Field(
        default_factory=list, description="Ошибки товаров в наборе."
    )


class FbpDraftDirectRegistrateResponse(BaseModel):
    """Схема ответа перевода черновика в действующую поставку.

    Attributes:
        is_error: Признак наличия ошибки
        error: Ошибка регистрации поставки
        row_version: Версия записи
    """

    is_error: Optional[bool] = Field(
        None, description="Признак наличия ошибки."
    )
    error: Optional[FbpDraftDirectRegistrateError] = Field(
        None, description="Ошибка регистрации поставки."
    )
    row_version: Optional[int] = Field(
        None, description="Версия записи."
    )
