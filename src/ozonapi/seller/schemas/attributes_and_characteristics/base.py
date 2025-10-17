from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.localization import Language


class BaseLanguageRequest(BaseModel):
    """Базовая схема запроса с указанием языковой локали."""
    language: Optional[Language | str] = Field(
        Language.DEFAULT, description="Язык в ответе."
    )


class BaseAttributeRequest(BaseModel):
    """Базовая схема запроса с указанием категории и типа товаров."""
    type_id: int = Field(
        ..., description="Идентификатор типа товара. Можно получить с помощью метода description_category_tree()."
    )
    description_category_id: int = Field(
        ..., description="Идентификатор категории. Можно получить с помощью метода description_category_tree()."
    )


class BaseExtAttributeRequest(BaseAttributeRequest):
    """Базовая расширенная схема запроса с указанием дополнительных аттрибутов."""
    attribute_id: int = Field(
        ..., description="Идентификатор характеристики. Можно получить с помощью метода description_category_attribute()."
    )


class BaseDescriptionCategoryAttributeValuesItem(BaseModel):
    """Значения характеристики."""
    id: int = Field(
        ..., description="Идентификатор значения характеристики."
    )
    info: str = Field(
        ..., description="Дополнительное описание."
    )
    picture: str = Field(
        ..., description="Ссылка на изображение."
    )
    value: str = Field(
        ..., description="Значение характеристики товара."
    )


class BaseDescriptionCategoryAttributeValuesResponse(BaseModel):
    """Описывает схему ответа на запрос о получении справочных значений характеристик."""
    result: Optional[list[BaseDescriptionCategoryAttributeValuesItem]] = Field(
        default_factory=list, description="Список справочных значений характеристик."
    )