"""https://docs.ozon.ru/api/seller/#operation/DescriptionCategoryAPI_GetAttributes"""
from pydantic import BaseModel, Field

from ...common.enumerations.localization import Language
from .base import BaseAttributeRequest, BaseLanguageRequest


class DescriptionCategoryAttributeRequest(BaseAttributeRequest, BaseLanguageRequest):
    """Описывает схему запроса на получение характеристик для указанных категории и типа товара.

    Attributes:
        description_category_id: Идентификатор категории, можно получить с помощью метода description_category_tree()
        type_id: Идентификатор типа товара, можно получить с помощью метода description_category_tree()
        language (Language | str): Язык в ответе (опционально)
     """
    pass


class DescriptionCategoryAttributeItem(BaseModel):
    """Описание характеристик.

    Attributes:
        category_dependent: Признак зависимости значений словарного атрибута от категории
        description: Описание характеристики
        dictionary_id: Идентификатор справочника
        group_id: Идентификатор группы характеристик
        group_name: Название группы характеристик
        id: Идентификатор характеристики
        is_aspect: Признак аспектного атрибута
        is_collection: Признак характеристики как набора значений
        is_required: Признак обязательной характеристики
        name: Название характеристики
        type: Тип характеристики
        attribute_complex_id: Идентификатор комплексного атрибута
        max_value_count: Максимальное количество значений для атрибута
        complex_is_collection: Признак комплексной характеристики как набора значений
    """
    category_dependent: bool = Field(
        ..., description="""
        Признак, что значения словарного атрибута зависят от категории:
        true — у атрибута разные значения для каждой категории.
        false — у атрибута одинаковые значения для всех категорий.
        """
    )
    description: str = Field(
        ..., description="Описание характеристики."
    )
    dictionary_id: int = Field(
        ..., description="Идентификатор справочника."
    )
    group_id: int = Field(
        ..., description="Идентификатор группы характеристик."
    )
    group_name: str = Field(
        ..., description="Название группы характеристик."
    )
    id: int = Field(
        ..., description="Идентификатор характеристики."
    )
    is_aspect: bool = Field(
        ..., description="""
        Признак аспектного атрибута. Аспектный атрибут — характеристика, по которой отличаются товары одной модели.
        Например, у одежды и обуви одной модели могут быть разные расцветки и размеры. То есть цвет и размер — это аспектные атрибуты.
        Значения поля:
        true — атрибут аспектный и его нельзя изменить после поставки товара на склад или продажи со своего склада.
        false — атрибут не аспектный, можно изменить в любое время.
        """
    )
    is_collection: bool = Field(
        ..., description="""
        true, если характеристика — набор значений.
        false, если характеристика — одно значение.
        """
    )
    is_required: bool = Field(
        ..., description="""
        Признак обязательной характеристики:
        true — обязательная характеристика,
        false — характеристику можно не указывать.
        """
    )
    name: str = Field(
        ..., description="Название."
    )
    type: str = Field(
        ..., description="Тип характеристики."
    )
    attribute_complex_id: int = Field(
        ..., description="Идентификатор комплексного атрибута."
    )
    max_value_count: int = Field(
        ..., description="Максимальное количество значений для атрибута."
    )
    complex_is_collection: bool = Field(
        ..., description="""
        true, если комплексная характеристика — набор значений,
        false, если комплексная характеристика — одно значение.
        """
    )


class DescriptionCategoryAttributeResponse(BaseModel):
    """Описывает схему ответа на запрос о получении характеристик для указанных категории и типа товара.

    Attributes:
        result: Список характеристик категории
    """
    result: list[DescriptionCategoryAttributeItem]
