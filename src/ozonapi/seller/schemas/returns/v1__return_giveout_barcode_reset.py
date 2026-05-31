"""https://docs.ozon.ru/api/seller/#operation/GiveoutAPI_GiveoutBarcodeReset"""
from typing import Optional

from pydantic import BaseModel, Field


class ReturnGiveoutBarcodeResetResponse(BaseModel):
    """Описывает схему ответа на запрос генерации нового штрихкода (PNG).

    Notes:
        • Несмотря на заявленный в документации тип `image/png`, API возвращает JSON
          с полем `png` — содержимым PNG-изображения нового штрихкода в виде строки (base64).

    Attributes:
        png: Содержимое PNG-изображения нового штрихкода (base64)
    """
    png: Optional[str] = Field(
        None, description="Содержимое PNG-изображения нового штрихкода (base64)."
    )
