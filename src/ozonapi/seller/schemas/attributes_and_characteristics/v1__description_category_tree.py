"""https://docs.ozon.ru/api/seller/#operation/DescriptionCategoryAPI_GetTree"""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.localization import Language
from .base import BaseLanguageRequest


class DescriptionCategoryTreeRequest(BaseLanguageRequest):
    """Описывает схему запроса на получение категорий и типов для товаров в виде дерева.

    Attributes:
        language (Language | str): Язык в ответе (опционально)
    """
    pass


class DescriptionCategoryTreeItem(BaseModel):
    """Описание категории или типа товара.

    Attributes:
        description_category_id: Идентификатор категории
        category_name: Название категории
        children: Дерево подкатегорий
        disabled: Флаг возможности создания товаров в категории
        type_id: Идентификатор типа товара
        type_name: Название типа товара
    """
    description_category_id: Optional[int] = Field(
        None, description="Идентификатор категории."
    )
    category_name: Optional[str] = Field(
        None, description="Название категории."
    )
    children: Optional[list["DescriptionCategoryTreeItem"]] = Field(
        default_factory=list, description="Дерево подкатегорий."
    )
    disabled: bool = Field(
        ..., description="true, если в категории нельзя создавать товары. false, если можно."
    )
    type_id: Optional[int] = Field(
        None, description="Идентификатор типа товара."
    )
    type_name: Optional[str] = Field(
        None, description="Название типа товара."
    )


DescriptionCategoryTreeItem.model_rebuild()


class DescriptionCategoryTreeResponse(BaseModel):
    """Описывает схему ответа на запрос о получении дерева категорий и типов для товаров в виде дерева.

    Attributes:
        result: Дерево описаний категории и типов для товаров
    """
    result: list[DescriptionCategoryTreeItem] = Field(
        ..., description="Дерево описаний категории и типов для товаров."
    )
