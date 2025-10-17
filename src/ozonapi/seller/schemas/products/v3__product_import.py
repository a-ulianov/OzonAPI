"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_ImportProductsV3"""
from typing import Optional, Literal

from pydantic import BaseModel, Field

from .base import BaseProductInfo
from ...common.enumerations.localization import CurrencyCode
from ...common.enumerations.products import ServiceType
from ...common.enumerations.prices import VAT, PromotionType, PromotionOperation


class ProductImportRequestItemPDFListItem(BaseModel):
    """Описание PDF-документа.

    Attributes:
        index: Индекс документа в хранилище
        name: Название файла
        src_url: Ссылка на документ
    """
    index: int = Field(
        ..., description="Индекс документа в хранилище, который задаёт порядок."
    )
    name: str = Field(
        ..., description="Название файла."
    )
    src_url: str = Field(
        ..., description="Ссылка на документ."
    )


class ProductImportRequestItemPromotion(BaseModel):
    """Акции.

    Attributes:
        operation: Атрибут для действий с акцией (опционально)
        type: Тип акции (опционально)
    """
    operation: Optional[PromotionOperation] = Field(
        PromotionOperation.UNKNOWN, description="Атрибут для действий с акцией."
    )
    type: Optional[PromotionType] = Field(
        PromotionType.REVIEWS_PROMO, description="Тип акции."
    )


class ProductImportItem(BaseProductInfo):
    """Описывает схему добавляемого товара.

    Attributes:
        attributes: Массив с характеристиками товара (опционально, зависит от применения и специфики товара)
        barcode: Штрихкод товара (опционально)
        color_image: Маркетинговый цвет (опционально)
        complex_attributes: Массив характеристик с вложенными атрибутами (опционально, зависит от применения)
        currency_code: Валюта цен (опционально)
        depth: Глубина упаковки
        description_category_id: Идентификатор категории
        new_description_category_id: Новый идентификатор категории (опционально)
        dimension_unit: Единица измерения габаритов
        geo_names: Геоограничения (опционально)
        height: Высота упаковки
        images: Массив изображений
        images360: Массив изображений 360 (опционально)
        name: Название товара
        offer_id: Идентификатор товара в системе продавца - артикул
        old_price: Цена до скидок (опционально)
        pdf_list: Список PDF-документов (опционально)
        price: Цена товара с учётом скидок
        primary_image: Ссылка на главное изображение товара
        promotions: Список акций (опционально)
        service_type: Тип сервиса (опционально)
        type_id: Идентификатор типа товара
        vat: Ставка НДС для товара
        weight: Вес товара в упаковке
        weight_unit: Единица измерения веса
        width: Ширина упаковки
    """
    currency_code: Optional[CurrencyCode] = Field(
        CurrencyCode.RUB, description="Валюта цен. Переданное значение должно совпадать с валютой, которая установлена в настройках личного кабинета."
    )
    new_description_category_id: Optional[int] = Field(
        ..., description="Новый идентификатор категории. Укажите его, если нужно изменить текущую категорию товара."
    )
    geo_names: Optional[list[str]] = Field(
        None, description="Геоограничения — при необходимости заполните параметр в личном кабинете при создании или редактировании товара."
    )
    images360: Optional[list[str]] = Field(
        None, description="Массив изображений 360 (максимум 70 ссылок на PNG или JPG)."
    )
    old_price: Optional[str] = Field(
        None, description="Цена до скидок (будет зачёркнута на карточке товара). Указывается в рублях. Разделитель дробной части — точка, до двух знаков после точки."
    )
    pdf_list: Optional[list[ProductImportRequestItemPDFListItem]] = Field(
        None, description="Список PDF-документов."
    )
    price: str = Field(
        ..., description="Цена товара с учётом скидок, отображается на карточке товара. Указывается в рублях. Разделитель дробной части — точка, до двух знаков после точки."
    )
    promotions: Optional[list[ProductImportRequestItemPromotion]] = Field(
        [ProductImportRequestItemPromotion(), ], description="Список акций."
    )
    service_type: Optional[ServiceType] = Field(
        ServiceType.IS_CODE_SERVICE, description="Тип сервиса (параметр не задокументирован)."
    )
    vat: VAT = Field(
        ..., description="Ставка НДС для товара."
    )


class ProductImportRequest(BaseModel):
    """Описывает схему запроса для создания товаров и обновления информации о них.

    Attributes:
        items: Товары
    """
    items: list[ProductImportItem] = Field(
        ..., description="Товары (максимум 100).",
        max_length=100,
    )


class ProductImportResponseResult(BaseModel):
    """Описывает схему результата выполнения запроса на загрузку и обновление товаров.

    Attributes:
        task_id: Номер задания на обновление товаров (чтобы проверить статус обновления, передайте полученное значение в метод product_import_info())
    """
    task_id: int = Field(
        ..., description="""
        Номер задания на загрузку или обновление товаров.
        Чтобы проверить статус обновления, передайте полученное значение в метод product_import_info().
        """
    )


class ProductImportResponse(BaseModel):
    """Описывает схему ответа на запрос создания товаров и обновления информации о них.

    Attributes:
        result: Результат выполнения запроса на загрузку и обновление товаров
    """
    result: ProductImportResponseResult = Field(
        ..., description="Результат выполнения запроса на загрузку и обновление товаров."
    )