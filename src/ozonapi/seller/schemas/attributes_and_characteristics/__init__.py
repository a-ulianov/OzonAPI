"""Описывает модели методов раздела Атрибуты и характеристики Ozon.
https://docs.ozon.ru/api/seller/?__rr=1#tag/CategoryAPI
"""
__all__ = [
    "DescriptionCategoryAttributeItem",
    "DescriptionCategoryAttributeRequest",
    "DescriptionCategoryAttributeResponse",
    "DescriptionCategoryAttributeValuesRequest",
    "DescriptionCategoryAttributeValuesResponse",
    "DescriptionCategoryAttributeValuesSearchRequest",
    "DescriptionCategoryAttributeValuesSearchResponse",
    "DescriptionCategoryTreeItem",
    "DescriptionCategoryTreeRequest",
    "DescriptionCategoryTreeResponse",
]

from .v1__description_category_attribute import DescriptionCategoryAttributeItem, \
    DescriptionCategoryAttributeRequest, DescriptionCategoryAttributeResponse
from .v1__description_category_attribute_values import DescriptionCategoryAttributeValuesRequest, \
    DescriptionCategoryAttributeValuesResponse
from .v1__description_category_attribute_values_search import DescriptionCategoryAttributeValuesSearchRequest, \
    DescriptionCategoryAttributeValuesSearchResponse
from .v1__description_category_tree import DescriptionCategoryTreeItem, DescriptionCategoryTreeRequest, \
    DescriptionCategoryTreeResponse