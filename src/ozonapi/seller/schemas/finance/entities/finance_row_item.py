"""Общая модель товара в строке финансового отчёта."""
from typing import Optional

from pydantic import BaseModel, Field


class FinanceRowItem(BaseModel):
    """Товар в строке отчёта о реализации.

    Attributes:
        sku: Идентификатор товара в системе Ozon — SKU
        offer_id: Идентификатор товара в системе продавца
        name: Наименование товара
        barcode: Штрихкод товара
    """
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца."
    )
    name: Optional[str] = Field(
        None, description="Наименование товара."
    )
    barcode: Optional[str] = Field(
        None, description="Штрихкод товара."
    )
