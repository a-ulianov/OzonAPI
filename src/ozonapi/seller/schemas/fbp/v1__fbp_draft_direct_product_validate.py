"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPDraft_FbpDraftDirectProductValidate"""
from typing import Optional

from pydantic import BaseModel, Field


class FbpProductValidateSkuItem(BaseModel):
    """Товар для проверки перед поставкой на склад партнёра.

    Attributes:
        sku: Идентификатор товара в системе Ozon — SKU
        count: Количество товара
    """

    sku: int = Field(..., description="Идентификатор товара в системе Ozon — SKU.")
    count: int = Field(..., description="Количество товара.")


class FbpDraftDirectProductValidateRequest(BaseModel):
    """Схема запроса проверки списка товаров для склада партнёра.

    Attributes:
        skus: Список товаров для проверки
        warehouse_id: Идентификатор склада
    """

    skus: list[FbpProductValidateSkuItem] = Field(
        default_factory=list, description="Список товаров для проверки."
    )
    warehouse_id: int = Field(..., description="Идентификатор склада.")


class FbpProductValidateApprovedItem(BaseModel):
    """Принятый товар после проверки.

    Attributes:
        sku: Идентификатор товара в системе Ozon — SKU
        offer_id: Артикул товара в системе продавца
        name: Название товара
        barcode: Штрихкод товара
        icon_name: Название иконки товара
        quantity: Количество товара
        volume: Объём товара
    """

    sku: Optional[int] = Field(None, description="Идентификатор товара в системе Ozon — SKU.")
    offer_id: Optional[str] = Field(None, description="Артикул товара в системе продавца.")
    name: Optional[str] = Field(None, description="Название товара.")
    barcode: Optional[str] = Field(None, description="Штрихкод товара.")
    icon_name: Optional[str] = Field(None, description="Название иконки товара.")
    quantity: Optional[int] = Field(None, description="Количество товара.")
    volume: Optional[float] = Field(None, description="Объём товара.")


class FbpProductValidateRejectedItem(BaseModel):
    """Отклонённый товар после проверки.

    Attributes:
        sku: Идентификатор товара в системе Ozon — SKU
        offer_id: Артикул товара в системе продавца
        name: Название товара
        barcode: Штрихкод товара
        icon_name: Название иконки товара
        quantity: Количество товара
        volume: Объём товара
        rejection_reasons: Причины отклонения (`OUT_OF_ASSORTMENT`, `INVALID`,
            `INCOMPATIBLE_WAREHOUSE`, `INVALID_BARCODE`, `NO_PRICE`, `BANNED` и др.)
    """

    sku: Optional[int] = Field(None, description="Идентификатор товара в системе Ozon — SKU.")
    offer_id: Optional[str] = Field(None, description="Артикул товара в системе продавца.")
    name: Optional[str] = Field(None, description="Название товара.")
    barcode: Optional[str] = Field(None, description="Штрихкод товара.")
    icon_name: Optional[str] = Field(None, description="Название иконки товара.")
    quantity: Optional[int] = Field(None, description="Количество товара.")
    volume: Optional[float] = Field(None, description="Объём товара.")
    rejection_reasons: list[str] = Field(
        default_factory=list,
        description="Причины отклонения товара (набор открытый — тип `str`)."
    )


class FbpDraftDirectProductValidateResponse(BaseModel):
    """Схема ответа проверки списка товаров для склада партнёра.

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
