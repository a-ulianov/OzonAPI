"""https://docs.ozon.ru/api/seller/#operation/GiveoutAPI_GiveoutBarcode"""
from typing import Optional

from pydantic import BaseModel, Field


class ReturnGiveoutBarcodeResponse(BaseModel):
    """Описывает схему ответа на запрос значения штрихкода для возвратных отгрузок.

    Attributes:
        barcode: Значение штрихкода в текстовом виде
    """
    barcode: Optional[str] = Field(
        None, description="Значение штрихкода в текстовом виде."
    )
