"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetProductPlacementZoneInfo"""
from typing import Optional

from pydantic import BaseModel, Field


class ProductPlacementZoneInfoRequest(BaseModel):
    """Схема запроса зон размещения товаров по SKU.

    Attributes:
        skus: Список идентификаторов товаров в системе Ozon — SKU
    """

    skus: list[str] = Field(
        default_factory=list,
        description="Список идентификаторов товаров в системе Ozon — SKU."
    )


class ProductPlacementZoneInfoProductPlacement(BaseModel):
    """Зона размещения товара перед поставкой.

    Attributes:
        sku: Идентификатор товара в системе Ozon — SKU
        placement_zone: Зона размещения товара. Известные значения: `UNSPECIFIED`,
            `CLOSED_ZONE`, `DANGEROUS_GOODS`, `PRODUCTS`, `SORT`, `NON_SORT`,
            `OVERSIZE`, `JEWELRY`, `UNRESOLVED` (набор открытый — тип `str`)
    """

    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    placement_zone: Optional[str] = Field(
        None,
        description="Зона размещения товара. Известные значения: `UNSPECIFIED`, "
                    "`CLOSED_ZONE`, `DANGEROUS_GOODS`, `PRODUCTS`, `SORT`, `NON_SORT`, "
                    "`OVERSIZE`, `JEWELRY`, `UNRESOLVED` (набор открытый — тип `str`)."
    )


class ProductPlacementZoneInfoResponse(BaseModel):
    """Схема ответа со списком зон размещения товаров.

    Attributes:
        products_placement: Список товаров с их зонами размещения
    """

    products_placement: list[ProductPlacementZoneInfoProductPlacement] = Field(
        default_factory=list,
        description="Список товаров с их зонами размещения."
    )
