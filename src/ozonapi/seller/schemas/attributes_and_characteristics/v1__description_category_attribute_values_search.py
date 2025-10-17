"""https://docs.ozon.ru/api/seller/#operation/DescriptionCategoryAPI_SearchAttributeValues"""
from typing import Optional

from pydantic import Field

from ...schemas.attributes_and_characteristics.base import BaseExtAttributeRequest, \
    BaseDescriptionCategoryAttributeValuesResponse


class DescriptionCategoryAttributeValuesSearchRequest(BaseExtAttributeRequest):
    """Описывает схему запроса на получение справочных значений характеристик по заданному значению value в запросе.

    Attributes:
        attribute_id: Идентификатор характеристики, можно получить с помощью метода description_category_attribute()
        description_category_id: Идентификатор категории, можно получить с помощью метода description_category_tree()
        type_id: Идентификатор типа товара, можно получить с помощью метода description_category_tree()
        value: Значение, по которому система будет искать справочные значения (минимум — 2 символа)
        limit: Количество значений в ответе (опционально, максимум 100)
    """
    limit: Optional[int] = Field(
        100, description="Количество значений в ответе.",
        ge=1, le=100
    )
    value: str = Field(
        ..., description="Значение, по которому система будет искать справочные значения. Минимум — 2 символа.",
        min_length=2
    )


class DescriptionCategoryAttributeValuesSearchResponse(BaseDescriptionCategoryAttributeValuesResponse):
    """Описывает схему ответа на запрос о получении справочных значений характеристик по заданному значению value.

    Attributes:
        result (list[BaseDescriptionCategoryAttributeValuesItem]): Список справочных значений характеристик
    """
    pass