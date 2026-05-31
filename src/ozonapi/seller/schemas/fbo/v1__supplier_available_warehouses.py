"""https://docs.ozon.com/api/seller/?#operation/WarehouseAPI_AvailableWarehouses"""
from typing import Any, Optional

from pydantic import BaseModel, Field


class SupplierAvailableWarehousesResponse(BaseModel):
    """Описывает схему ответа на запрос загруженности складов Ozon.

    Notes:
        • Структура поля `result` в спецификации Ozon не типизирована;
          сохраняется «как есть» и уточняется по реальному ответу API.

    Attributes:
        result: Результат работы метода (загруженность складов)
    """
    result: Optional[Any] = Field(
        None, description="Результат работы метода (загруженность складов)."
    )
