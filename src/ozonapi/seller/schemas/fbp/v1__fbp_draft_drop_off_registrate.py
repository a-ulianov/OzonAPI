"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPDraft_FbpDraftDropOffRegistrate"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import FbpBundleItemError


class FbpDraftDropOffRegistrateRequest(BaseModel):
    """Схема запроса перевода drop-off черновика в действующую поставку.

    Attributes:
        supply_id: Идентификатор поставки
        row_version: Версия записи
    """

    supply_id: str = Field(..., description="Идентификатор поставки.")
    row_version: int = Field(..., description="Версия записи.")


class FbpDraftDropOffRegistrateError(BaseModel):
    """Ошибка регистрации drop-off поставки FBP.

    Attributes:
        order_error: Код ошибки заявки (`INVALID_NUMBER_OF_PACKAGE_UNITS`,
            `DROP_OFF_POINTS_IS_EMPTY`, `DRAFT_LOCKED`, `WAS_CANCELLED`,
            `INTERNAL_ERROR` и др.)
        bundle_errors: Ошибки товаров в наборе
    """

    order_error: Optional[str] = Field(
        None,
        description="Код ошибки заявки на поставку (набор открытый — тип `str`)."
    )
    bundle_errors: list[FbpBundleItemError] = Field(
        default_factory=list, description="Ошибки товаров в наборе."
    )


class FbpDraftDropOffRegistrateResponse(BaseModel):
    """Схема ответа перевода drop-off черновика в действующую поставку.

    Attributes:
        is_error: Признак наличия ошибки
        error: Ошибка регистрации поставки
        row_version: Версия записи
    """

    is_error: Optional[bool] = Field(
        None, description="Признак наличия ошибки."
    )
    error: Optional[FbpDraftDropOffRegistrateError] = Field(
        None, description="Ошибка регистрации поставки."
    )
    row_version: Optional[int] = Field(
        None, description="Версия записи."
    )
