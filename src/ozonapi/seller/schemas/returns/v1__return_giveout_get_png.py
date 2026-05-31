"""https://docs.ozon.ru/api/seller/#operation/GiveoutAPI_GiveoutGetPNG"""
from typing import Optional

from pydantic import BaseModel, Field


class ReturnGiveoutGetPNGResponse(BaseModel):
    """Описывает схему ответа на запрос штрихкода возвратной отгрузки в формате PNG.

    Notes:
        • Несмотря на заявленный в документации тип `image/png`, API возвращает JSON
          с полем `png` — содержимым PNG-изображения в виде строки (base64).

    Attributes:
        png: Содержимое PNG-изображения (base64)
    """
    png: Optional[str] = Field(
        None, description="Содержимое PNG-изображения (base64)."
    )
