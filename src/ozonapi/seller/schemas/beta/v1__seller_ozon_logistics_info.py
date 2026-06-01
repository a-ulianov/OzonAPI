"""https://docs.ozon.ru/api/seller/#operation/SellerAPI_SellerOzonLogisticsInfo"""
from pydantic import BaseModel, Field


class SellerOzonLogisticsInfoResponse(BaseModel):
    """Схема ответа с информацией о подключении продавца к Ozon Логистике.

    Attributes:
        available_schemas: Доступные продавцу схемы работы (`UNKNOWN`, `FBO`, `FBS`)
        ozon_logistics_enabled: Признак подключения продавца к Ozon Логистике
    """

    available_schemas: list[str] = Field(
        default_factory=list,
        description="Список доступных продавцу схем работы. Известные значения: "
                    "`UNKNOWN`, `FBO`, `FBS` (набор открытый — тип `str`)."
    )
    ozon_logistics_enabled: bool = Field(
        False,
        description="Признак того, что продавец подключён к Ozon Логистике."
    )
