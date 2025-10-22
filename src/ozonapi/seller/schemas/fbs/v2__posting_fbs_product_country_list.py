"""https://docs.ozon.ru/api/seller/?__rr=1#operation/PostingAPI_ListCountryProductFbsPostingV2"""
from typing import Optional

from pydantic import BaseModel, Field


class PostingFBSProductCountryListRequest(BaseModel):
    """Описывает схему запроса для получения списка доступных стран-изготовителей и их ISO кодов.

    Attributes:
        name_search: Поисковая строка
    """
    model_config = {'frozen': True}

    name_search: Optional[str] = Field(
        default_factory=str, description="Поисковая строка."
    )


class PostingFBSProductCountryListResult(BaseModel):
    """Информация о стране-изготовителе.

    Attributes:
        name: Название страны на русском языке
        country_iso_code: ISO код страны
    """
    name: str = Field(
        ..., description="Название страны на русском языке."
    )
    country_iso_code: str = Field(
        ..., description="ISO код страны."
    )


class PostingFBSProductCountryListResponse(BaseModel):
    """Описывает схему ответа на запрос о получении списка доступных стран-изготовителей и их ISO кодов.

    Attributes:
        result: Список стран-изготовителей и ISO коды
    """
    model_config = {'frozen': True}

    result: Optional[list[PostingFBSProductCountryListResult]] = Field(
        default_factory=list, description="Список стран-изготовителей и ISO коды."
    )