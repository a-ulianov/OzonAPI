from typing import Optional, Literal

from pydantic import BaseModel, Field

from ...common.enumerations.products import Visibility, DimensionUnit, WeightUnit


class BaseProductListFilter(BaseModel):
    """Модель фильтра для получения списка товаров.
    Позволяет фильтровать товары по артикулу, идентификатору и видимости.

    Attributes:
        offer_id: Фильтр по параметру offer_id
        product_id: Фильтр по параметру product_id
        visibility: Видимость товара
    """
    offer_id: Optional[list[str]] = Field(
        None, description="Фильтр по параметру offer_id. Вы можете передавать список значений."
    )
    product_id: Optional[list[int]] = Field(
        None, description="Фильтр по параметру product_id. Вы можете передавать список значений."
    )
    visibility: Optional[Visibility] = Field(
        Visibility.ALL, description="Видимость товара."
    )


class BaseProductInfoListRequest(BaseModel):
    """Описывает схему запроса для получения информации о товарах по их идентификаторам.

    Attributes:
        offer_id: Идентификаторы товаров в системе продавца (опционально)
        product_id: Идентификаторы товаров в системе Ozon (опционально)
        sku: Идентификаторы товаров в системе Ozon (опционально)
    """
    offer_id: Optional[list[str]] = Field(
        None, description="Идентификаторы товаров в системе продавца — артикулы."
    )
    product_id: Optional[list[int]] = Field(
        None, description="Идентификаторы товаров в системе Ozon — product_id."
    )
    sku: Optional[list[int]] = Field(
        None, description="Идентификаторы товаров в системе Ozon — SKU."
    )


class BaseProductProductIdListRequest(BaseModel):
    """Базовая схема для запросов со списком product_id.

    Attributes:
        product_id: Список product_id (максимум 100 идентификаторов)
    """
    product_id: list[int] = Field(
        ..., description="Список product_id (максимум 100 идентификаторов)",
        min_length=1, max_length=100,
    )


class BaseSimpleBoolResponse(BaseModel):
    """Базовая схема, описывающая простой логический ответ."""
    result: bool = Field(
        ..., description="Результат обработки запроса: true, если успешно"
    )


class ProductAttributeValue(BaseModel):
    """Вложенное значение характеристики.

    Attributes:
        dictionary_value_id: Идентификатор характеристики в словаре
        value: Значение характеристики товара
    """
    dictionary_value_id: Optional[int] = Field(
        None, description="Идентификатор характеристики в словаре."
    )
    value: Optional[str] = Field(
        None, description="Значение характеристики товара."
    )


class ProductAttribute(BaseModel):
    """Описание характеристики.
    Характеристики отличаются для разных категорий — их можно посмотреть в Базе знаний продавца или через API.

    Attributes:
        complex_id: Идентификатор характеристики с вложенными свойствами (опционально, если характеристика не является комплексной)
        id: Идентификатор характеристики
        values: Массив вложенных значений характеристики
    """
    complex_id: Optional[int] = Field(
        None, description="Идентификатор характеристики, которая поддерживает вложенные свойства."
    )
    id: int = Field(
        ..., description="Идентификатор характеристики."
    )
    values: Optional[list[ProductAttributeValue]] = Field(
        None, description="Массив вложенных значений характеристики."
    )


class BaseProductInfo(BaseModel):
    attributes: Optional[list[ProductAttribute]] = Field(
        None, description="Массив с характеристиками товара."
    )
    barcode: Optional[str] = Field(
        None, description="Штрихкод товара."
    )
    description_category_id: int = Field(
        ..., description="Идентификатор категории (можно получить методом description_category_tree())."
    )
    color_image: Optional[str] = Field(
        None, description="Маркетинговый цвет (ссылка на изображение JPG)."
    )
    complex_attributes: Optional[list[ProductAttribute]] = Field(
        None, description="Массив характеристик, у которых есть вложенные атрибуты."
    )
    depth: int = Field(
        ..., description="Глубина упаковки."
    )
    dimension_unit: DimensionUnit | Literal["mm", "cm", "in"] = Field(
        ..., description="Единица измерения габаритов."
    )
    height: int = Field(
        ..., description="Высота упаковки."
    )
    images: Optional[list[str]] = Field(
        None, description="""
        Массив изображений (максимум 30 ссылок на PNG или JPG).
        Изображения показываются на сайте в таком же порядке, как в массиве.
        Если не передать значение primary_image, первое изображение в массиве будет главным для товара.

        """,
        max_length=30,
    )
    name: str = Field(
        ..., description="Название товара (максимум 500 символов).",
        max_length=500,
    )
    offer_id: str = Field(
        ..., description="Идентификатор товара в системе продавца — артикул (максимум 50 символов).",
        max_length=50,
    )
    primary_image: Optional[str] = Field(
        None, description="Ссылка на главное изображение товара (PNG или JPG)."
    )
    type_id: Optional[int] = Field(
        None, description="""
        Идентификатор типа товара. 
        Значения можно получить из такого же параметра type_id в ответе метода description_category_tree(). 
        При заполнении этого параметра можно не указывать в attibutes атрибут с параметром id:8229, 
        type_id будет использоваться в приоритете.        
        """
    )
    weight: int = Field(
        ..., description="Вес товара в упаковке."
    )
    weight_unit: WeightUnit | Literal["g", "kg", "lb"] = Field(
        ..., description="Единица измерения веса."
    )
    width: int = Field(
        ..., description="Ширина упаковки."
    )