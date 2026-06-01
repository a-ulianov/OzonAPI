"""Общие сущности раздела Накладные."""
from pydantic import BaseModel, Field


class InvoiceHsCode(BaseModel):
    """HS-код товара в счёте-фактуре.

    Attributes:
        code: HS-код товара
        sku: Идентификатор товара в системе Ozon — SKU
    """
    code: str = Field("", description="HS-код товара.")
    sku: str = Field("", description="Идентификатор товара в системе Ozon — SKU.")
