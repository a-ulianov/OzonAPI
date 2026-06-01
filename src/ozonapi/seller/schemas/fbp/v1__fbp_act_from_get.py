"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPSupply_FbpCheckActState"""
from typing import Optional

from pydantic import BaseModel, Field


class FbpActFromGetRequest(BaseModel):
    """Схема запроса статуса генерации акта приёмки.

    Attributes:
        file_uuid: Идентификатор файла акта
    """

    file_uuid: str = Field(..., description="Идентификатор файла акта.")


class FbpActFromGetResponse(BaseModel):
    """Схема ответа со статусом генерации акта приёмки.

    Attributes:
        status: Статус генерации (`NOT_EXIST`, `PROCESSING`, `EXIST`, `ERROR`)
        cdn_url: Ссылка на готовый файл акта
        error: Код ошибки генерации (`INVALID_COMPANY`, `FILE_NOT_FOUND`,
            `GENERATE_TIMEOUT_REACHED`, `GENERATION_ERROR`)
    """

    status: Optional[str] = Field(
        None,
        description="Статус генерации (`NOT_EXIST`, `PROCESSING`, `EXIST`, `ERROR`; "
                    "набор открытый — тип `str`)."
    )
    cdn_url: Optional[str] = Field(
        None, description="Ссылка на готовый файл акта."
    )
    error: Optional[str] = Field(
        None,
        description="Код ошибки генерации (набор открытый — тип `str`)."
    )
