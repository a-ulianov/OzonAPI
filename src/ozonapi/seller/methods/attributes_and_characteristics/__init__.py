__all__ = ["SellerCategoryAPI", ]

from .description_category_attribute import DescriptionCategoryAttributeMixin
from .description_category_attribute_values import DescriptionCategoryAttributeValuesMixin
from .description_category_attribute_values_search import DescriptionCategoryAttributeValuesSearchMixin
from .description_category_tree import DescriptionCategoryTreeMixin


class SellerCategoryAPI(
    DescriptionCategoryAttributeMixin,
    DescriptionCategoryAttributeValuesMixin,
    DescriptionCategoryAttributeValuesSearchMixin,
    DescriptionCategoryTreeMixin,
):
    """Реализует методы раздела Атрибуты и характеристики Ozon.

    References:
        https://docs.ozon.ru/api/seller/?__rr=1#tag/CategoryAPI
    """
    pass