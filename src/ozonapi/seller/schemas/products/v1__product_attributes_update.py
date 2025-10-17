"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductUpdateAttributes"""
from pydantic import BaseModel, Field


class ProductAttributesUpdateItemAttributeValue(BaseModel):
    """Вложенные значения характеристики.

    Attributes:
        dictionary_value_id: Идентификатор характеристики в словаре
        value: Значение характеристики товара
    """
    dictionary_value_id: int = Field(
        ..., description="Идентификатор характеристики в словаре."
    )
    value: str = Field(
        ..., description="Значение характеристики товара."
    )


class ProductAttributesUpdateItemAttribute(BaseModel):
    """Характеристики товара.

    Attributes:
        id: Идентификатор характеристики
        complex_id: Идентификатор характеристики, которая поддерживает вложенные свойства
        values: Массив вложенных значений характеристики
    """
    complex_id: int = Field(
        ..., description="""
        Идентификатор характеристики, которая поддерживает вложенные свойства.
        У каждой из вложенных характеристик может быть несколько вариантов значений.
        """
    )
    id: int = Field(
        ..., description="Идентификатор характеристики.",
    )
    values: list[ProductAttributesUpdateItemAttributeValue] = Field(
        ..., description="Массив вложенных значений характеристики.",
    )


class ProductAttributesUpdateItem(BaseModel):
    """Описывает необходимые для обновления товара данные.

    Attributes:
        offer_id: Артикул товара
        attributes: Характеристики товара
    """
    attributes: list[ProductAttributesUpdateItemAttribute] = Field(
        ..., description="Характеристики товара."
    )
    offer_id: str = Field(
        ..., description="Артикул товара."
    )


class ProductAttributesUpdateRequest(BaseModel):
    """Описывает схему запроса на обновление товаров и характеристик.

    Attributes:
        items: Товары и характеристики, которые нужно обновить.
    """
    items: list[ProductAttributesUpdateItem] = Field(
        ..., description="Список товаров с характеристиками, которые нужно обновить."
    )


class ProductAttributesUpdateResponse(BaseModel):
    """Описывает схему ответа на запрос об обновлении товаров и характеристик.

    Attributes:
        task_id: Номер задания на обновление товаров (чтобы проверить статус обновления, передайте полученное значение в метод product_import_info())
    """
    task_id: int = Field(
        ..., description="""
        Номер задания на обновление товаров.
        Чтобы проверить статус обновления, передайте полученное значение в метод product_import_info().
        """
    )