"""https://docs.ozon.ru/api/seller/?__rr=1#operation/DescriptionCategoryAPI_GetAttributeValues"""
from typing import Optional

from pydantic import Field

from ...common.enumerations.localization import Language
from .base import BaseExtAttributeRequest, BaseLanguageRequest, BaseDescriptionCategoryAttributeValuesResponse
from ..base import BaseResponseHasNext


class DescriptionCategoryAttributeValuesRequest(BaseExtAttributeRequest, BaseLanguageRequest):
    """Описывает схему запроса на получение справочника значений характеристики.

    Attributes:
        attribute_id: Идентификатор характеристики, можно получить с помощью метода description_category_attribute()
        description_category_id: Идентификатор категории, можно получить с помощью метода description_category_tree()
        type_id: Идентификатор типа товара, можно получить с помощью метода description_category_tree()
        language (Language | str): Язык в ответе (опционально)
        last_value_id: Идентификатор справочника, с которого нужно начать ответ (опционально, если равен 10, то в ответе будут справочники, начиная с одиннадцатого)
        limit: Количество значений в ответе (опционально, максимум 2000)
    """
    last_value_id: Optional[int] = Field(
        None, description="Идентификатор справочника, с которого нужно начать ответ. Если last_value_id — 10, то в ответе будут справочники, начиная с одиннадцатого."
    )
    limit: Optional[int] = Field(
        2000, description="Количество значений в ответе.",
        ge=1, le=2000
    )


class DescriptionCategoryAttributeValuesResponse(BaseDescriptionCategoryAttributeValuesResponse, BaseResponseHasNext):
    """Описывает схему ответа на запрос о получении справочных значений характеристик.

    Attributes:
        result (list[BaseDescriptionCategoryAttributeValuesItem]): Список справочных значений характеристик
        has_next (bool): Признак, что в ответе вернулась только часть значений
    """
    pass