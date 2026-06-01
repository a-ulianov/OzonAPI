"""Общие сущности валидации черновиков и поставок FBP."""
from typing import Optional

from pydantic import BaseModel, Field


class FbpOrderDraftValidationError(BaseModel):
    """Ошибка валидации черновика поставки FBP.

    Attributes:
        errors: Коды ошибок валидации (`ERROR_TYPE_UNSPECIFIED`,
            `ORDER_DRAFT_LOCKED`, `DELIVERY_*`, `INVALID_BUSINESS_FLOW`,
            `SUPPLY_TYPE_NOT_SUPPORTED`, `INVALID_STATE`)
    """

    errors: list[str] = Field(
        default_factory=list,
        description="Коды ошибок валидации черновика (набор открытый — тип `str`)."
    )


class FbpBundleItemError(BaseModel):
    """Ошибки товара в наборе при регистрации поставки FBP.

    Attributes:
        sku: Идентификатор товара в системе Ozon — SKU
        errors: Коды ошибок товара (`OUT_OF_ASSORTMENT`, `INVALID`,
            `INCOMPATIBLE_WAREHOUSE`, `INVALID_BARCODE`, `MULTIPLICITY`, `NO_PRICE`,
            `BANNED`, `DUPLICATE_ITEMS`, `ZERO_QUANTITY`, `QUANTITY_GREATER_THEN_MAX`,
            `NO_SALES`, `SURPLUS`, `AVAILABILITY_IS_EMPTY`)
    """

    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    errors: list[str] = Field(
        default_factory=list,
        description="Коды ошибок товара в наборе (набор открытый — тип `str`)."
    )
