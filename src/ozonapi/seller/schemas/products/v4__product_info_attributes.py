"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetProductAttributesV4"""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.requests import SortingDirection, ProductsSortingBy
from ..base import BaseResponseLastId, BaseRequestLastId
from .base import BaseProductListFilter, BaseProductInfo, BaseProductInfoListRequest


class ProductInfoAttributesFilter(BaseProductInfoListRequest, BaseProductListFilter):
    """Модель фильтра для получения списка товаров.
    Позволяет фильтровать товары по артикулу, идентификатору и видимости.

    Attributes:
        offer_id: Фильтр по списку offer_id
        product_id: Фильтр по списку product_id
        sku: Фильтр по списку sku
        visibility: Видимость товара (ALL, VISIBLE, INVISIBLE)
    """
    pass


class ProductInfoAttributesRequest(BaseRequestLastId):
    """Запрос на получение описаний характеристик товаров по идентификатору и видимости.

    Attributes:
        filter: Фильтр выборки
        last_id: Идентификатор последнего значения на странице
        limit: Количество значений на странице
        sort_by: Параметр сортировки
        sort_dir: Направление сортировки
    """
    filter: Optional[ProductInfoAttributesFilter] = Field(
        default_factory=ProductInfoAttributesFilter.model_construct, description="Фильтр выборки."
    )
    limit: Optional[int] = Field(
        1000, description="Количество значений на странице (1-1000).",
        le=1000, ge=1,
    )
    sort_by: Optional[ProductsSortingBy] = Field(
        None, description="Параметр сортировки."
    )
    sort_dir: Optional[SortingDirection] = Field(
        None, description="Направление сортировки."
    )


class ProductInfoAttributesPdfFile(BaseModel):
    """PDF-файл документа.

    Attributes:
        file_name: Путь к PDF-файлу
        name: Название файла
    """
    file_name: Optional[str] = Field(
        None, description="Путь к PDF-файлу."
    )
    name: Optional[str] = Field(
        None, description="Название файла."
    )


class ProductInfoAttributesModelInfo(BaseModel):
    """Информация о модели.

    Attributes:
        model_id: Идентификатор модели
        count: Количество объединённых товаров модели
    """
    model_id: Optional[int] = Field(
        None, description="Идентификатор модели."
    )
    count: Optional[int] = Field(
        None, description="Количество объединённых товаров модели."
    )


class ProductInfoAttributesItem(BaseProductInfo):
    """Описание характеристик товара.

    Attributes:
        attributes: Массив с характеристиками товара (опционально, зависит от применения и специфики товара)
        attributes_with_defaults: Список ID характеристик со значением по умолчанию
        barcode: Штрихкод товара (опционально)
        barcodes: Все штрихкоды товара
        color_image: Маркетинговый цвет (опционально)
        complex_attributes: Массив характеристик с вложенными атрибутами (опционально, зависит от применения)
        depth: Глубина упаковки
        description_category_id: Идентификатор категории
        dimension_unit: Единица измерения габаритов
        height: Высота упаковки
        id: ID товара
        images: Массив изображений
        model_info: Информация о модели
        name: Название товара
        offer_id: Идентификатор товара в системе продавца - артикул
        pdf_list: Массив PDF-файлов
        primary_image: Ссылка на главное изображение товара
        sku: SKU товара
        type_id: Идентификатор типа товара
        weight: Вес товара в упаковке
        weight_unit: Единица измерения веса
        width: Ширина упаковки
    """
    attributes_with_defaults: Optional[list[int]] = Field(
        default_factory=list,
        description="Список ID характеристик со значением по умолчанию.",
    )
    barcodes: Optional[list[str]] = Field(
        default_factory=list, description="Все штрихкоды товара."
    )
    id: int = Field(
        ..., description="ID товара (product_id)."
    )
    model_info: Optional[ProductInfoAttributesModelInfo] = Field(
        None, description="Информация о модели."
    )
    pdf_list: Optional[list[ProductInfoAttributesPdfFile]] = Field(
        default_factory=list, description="Массив PDF-файлов."
    )
    sku: Optional[int] = Field(
        None, description="SKU товара."
    )


class ProductInfoAttributesResponse(BaseResponseLastId):
    """Описывает схему ответа на запрос описаний характеристик товаров.

    Attributes:
        result: Результаты запроса
        last_id: Идентификатор последнего значения на странице
        total: Общее количество товаров в выборке
    """
    result: list[ProductInfoAttributesItem] = Field(
        default_factory=list, description="Результаты запроса."
    )