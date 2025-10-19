"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetProductInfoList"""
import datetime
from typing import Optional

from pydantic import BaseModel, Field, model_validator

from .base import BaseProductInfoListRequest
from ...common.enumerations.localization import CurrencyCode
from ...common.enumerations.products import ErrorLevel, ShipmentType
from ...common.enumerations.prices import VAT, ColorIndexWithPrefix


class ProductInfoListRequest(BaseProductInfoListRequest):
    """Описывает схему запроса для получения информации о товарах по их идентификаторам.

    Attributes:
        offer_id: Идентификаторы товаров в системе продавца (опционально)
        product_id: Идентификаторы товаров в системе Ozon (опционально)
        sku: Идентификаторы товаров в системе Ozon (опционально)
    """
    @model_validator(mode='after')
    def validate_total_items_count(self):
        """Проверяет, что сумма элементов по всем параметрам не превышает 1000."""
        fields_to_check = [self.offer_id, self.product_id, self.sku]

        total_count = sum(len(field) for field in fields_to_check if field is not None)

        if total_count > 1000:
            raise ValueError(
                f"Общее количество идентификаторов ({total_count}) в запросе превышает максимально допустимое значение 1000."
            )

        return self


class ProductInfoListErrorTextsParams(BaseModel):
    """Параметр, в котором допущена ошибка.

    Attributes:
        name: Название параметра
        value: Значение параметра
    """
    name: Optional[str] = Field(
        None, description="Название параметра."
    )
    value: Optional[str] = Field(
        None, description="Значение параметра."
    )


class ProductInfoListErrorTexts(BaseModel):
    """Описание ошибок.

    Attributes:
        attribute_name: Название атрибута с ошибкой
        description: Описание ошибки
        hint_code: Код ошибки в системе Ozon
        message: Текст ошибки
        params: Параметры с ошибкой
        short_description: Краткое описание ошибки
    """
    attribute_name: Optional[str] = Field(
        None, description="Название атрибута, в котором произошла ошибка."
    )
    description: Optional[str] = Field(
        None, description="Описание ошибки."
    )
    hint_code: Optional[str] = Field(
        None, description="Код ошибки в системе Ozon."
    )
    message: Optional[str] = Field(
        None, description="Текст ошибки."
    )
    params: Optional[list[ProductInfoListErrorTextsParams]] = Field(
        default_factory=list, description="В каких параметрах допущена ошибка."
    )
    short_description: Optional[str] = Field(
        None, description="Краткое описание ошибки."
    )


class ProductInfoListError(BaseModel):
    """Информация об ошибках при создании или валидации товара.

    Attributes:
        attribute_id: Идентификатор характеристики
        code: Код ошибки
        field: Поле с ошибкой
        level: Уровень ошибки
        state: Статус товара с ошибкой
        texts: Описание ошибок
    """
    attribute_id: Optional[int] = Field(
        None, description="Идентификатор характеристики."
    )
    code: Optional[str] = Field(
        None, description="Код ошибки."
    )
    field: Optional[str] = Field(
        None, description="Поле, в котором найдена ошибка."
    )
    level: Optional[ErrorLevel] = Field(
        None, description="Уровень ошибки."
    )
    state: Optional[str] = Field(
        None, description="Статус товара, в котором произошла ошибка."
    )
    texts: Optional[ProductInfoListErrorTexts] = Field(
        None, description="Описание ошибок."
    )


class ProductInfoListCommission(BaseModel):
    """Информация о комиссиях.

    Attributes:
        delivery_amount: Стоимость доставки
        percent: Процент комиссии
        return_amount: Стоимость возврата
        sale_schema: Схема продажи
        value: Сумма комиссии
        currency_code: Код валюты
    """
    delivery_amount: Optional[float] = Field(
        None, description="Стоимость доставки."
    )
    percent: float = Field(
        ..., description="Процент комиссии."
    )
    return_amount: Optional[float] = Field(
        None, description="Стоимость возврата."
    )
    sale_schema: str = Field(
        ..., description="Схема продажи."
    )
    value: float = Field(
        ..., description="Сумма комиссии."
    )
    currency_code: Optional[CurrencyCode | str] = Field(
        None, description="Код валюты."
    )


class ProductInfoListPriceIndexData(BaseModel):
    """Базовая схема ценовых индексов товара.

    Attributes:
        minimal_price: Минимальная цена
        minimal_price_currency: Валюта цены
        price_index_value: Значение индекса цены
    """
    minimal_price: str | None = Field(
        ..., description="Минимальная цена."
    )
    minimal_price_currency: str | None = Field(
        ..., description="Валюта цены."
    )
    price_index_value: float = Field(
        ..., description="Значение индекса цены."
    )


class ProductInfoListPriceIndexes(BaseModel):
    """Ценовые индексы товара.

    Attributes:
        color_index: Вид индекса цен
        external_index_data: Цена товара у конкурентов на других площадках
        ozon_index_data: Цена товара у конкурентов на Ozon
        self_marketplaces_index_data: Цена товара на других площадках
    """
    color_index: ColorIndexWithPrefix = Field(
        ..., description="Вид индекса цен."
    )
    external_index_data: ProductInfoListPriceIndexData | None = Field(
        ..., description="Цена товара у конкурентов на других площадках."
    )
    ozon_index_data: ProductInfoListPriceIndexData | None = Field(
        ..., description="Цена товара у конкурентов на Ozon."
    )
    self_marketplaces_index_data: ProductInfoListPriceIndexData | None = Field(
        ..., description="Цена товара на других площадках."
    )


class ProductInfoListModelInfo(BaseModel):
    """Информация о модели товара.

    Attributes:
        count: Количество товаров в ответе
        model_id: Количество товаров в ответе
    """
    model_config = {"protected_namespaces": ()}

    count: int = Field(
        ..., description="Количество товаров в ответе."
    )
    model_id: int = Field(
        ..., description="Количество товаров в ответе."
    )


class ProductInfoListSource(BaseModel):
    """Информация о созданном товара.

    Attributes:
        sku: Идентификатор товара на Ozon
        source: Схема продажи
        created_at: Дата создания товара
        quant_code: Список квантов с товарами
        shipment_type: Тип упаковки
    """
    sku: int = Field(
        ..., description="Идентификатор товара на Ozon."
    )
    source: str = Field(
        ..., description="Схема продажи."
    )
    created_at: datetime.datetime = Field(
        ..., description="Дата создания товара."
    )
    quant_code: str = Field(
        ..., description="Список квантов с товарами."
    )
    shipment_type: ShipmentType = Field(
        ..., description="Тип упаковки."
    )


class ProductInfoListStockStatus(BaseModel):
    """Остатки товара по схеме продаж.

    Attributes:
        present: Сейчас на складе
        reserved: Зарезервировано
        sku: Идентификатор товара в системе Ozon
        source: Схема продаж
    """
    present: int = Field(
        ..., description="Сейчас на складе."
    )
    reserved: int = Field(
        ..., description="Зарезервировано."
    )
    sku: int = Field(
        ..., description="Идентификатор товара в системе Ozon — SKU."
    )
    source: str = Field(
        ..., description="Схема продаж."
    )


class ProductInfoListStatuses(BaseModel):
    """Описание состояний товара на Ozon.

    Attributes:
        status: Статус товара
        status_failed: Статус товара с ошибкой
        moderate_status: Статус модерации
        validation_status: Статус валидации
        status_name: Название статуса товара
        status_description: Описание статуса товара
        is_created: Признак корректного создания товара
        status_tooltip: Описание статуса
        status_updated_at: Время последнего изменения статуса
    """
    status: str = Field(
        ..., description="Статус товара."
    )
    status_failed: str = Field(
        ..., description="Статус товара, в котором возникла ошибка."
    )
    moderate_status: str = Field(
        ..., description="Статус модерации."
    )
    validation_status: str = Field(
        ..., description="Статус валидации."
    )
    status_name: str = Field(
        ..., description="Название статуса товара."
    )
    status_description: str = Field(
        ..., description="Описание статуса товара."
    )
    is_created: bool = Field(
        ..., description="Товар создан корректно."
    )
    status_tooltip: str = Field(
        ..., description="Описание статуса."
    )
    status_updated_at: datetime.datetime = Field(
        ..., description="Время последнего изменения статуса."
    )


class ProductInfoListStocks(BaseModel):
    """Информация об остатках товара.

    Attributes:
        has_stock: Наличие остатка на складах
        stocks: Информация об остатках по схемам продаж
    """
    has_stock: bool = Field(
        ..., description="Наличие остатка на складах."
    )
    stocks: Optional[list[ProductInfoListStockStatus]] = Field(
        default_factory=list, description="Информация об остатках по схемам продаж."
    )


class ProductInfoListVisibilityDetails(BaseModel):
    """Видимость товара.

    Attributes:
        has_price: Наличие установленной цены
        has_stock: Наличие остатка на складах
    """
    has_price: bool = Field(
        ..., description="На товар установлена цена."
    )
    has_stock: bool = Field(
        ..., description="Есть остаток на складах."
    )


class ProductInfoListItem(BaseModel):
    """Описание товара и товарной карточки.

    Attributes:
        barcodes: Все штрихкоды товара
        color_image: URL маркетингового цвета
        commissions: Применяемые комиссии
        created_at: Дата и время создания товара
        currency_code: Код валюты
        description_category_id: Идентификатор категории
        discounted_fbo_stocks: Остатки уценённого товара на складе Ozon
        errors: Информация об ошибках
        has_discounted_fbo_item: Наличие уцененных товаров на складе Ozon
        id: Идентификатор Ozon (product_id)
        images: Изображения товара
        images360: Изображения товара для 360
        is_archived: Признак архивации товарной карточки
        is_autoarchived: Признак автоматической архивации
        is_discounted: Признак уцененного товара
        is_kgt: Признак крупногабаритного товара
        is_prepayment_allowed: Возможность предоплаты
        is_super: Признак супер-товара
        marketing_price: Цена на товар с учетом акций
        min_price: Минимальная цена товара при бустинге
        model_info: Информация о модели товара
        name: Наименование товара
        offer_id: Идентификатор товара в системе продавца
        old_price: Цена до учёта скидок
        price: Текущая цена товара
        price_indexes: Ценовые индексы товара
        primary_image: Главное изображение
        sources: Информация об источниках схожих предложений
        statuses: Описание состояний товара на Ozon
        stocks: Информация об остатках товара
        type_id: Идентификатор типа товара
        updated_at: Дата и время обновления информации
        vat: Ставка НДС
        visibility_details: Настройки видимости товара
        volume_weight: Объемный вес товара
    """
    model_config = {"protected_namespaces": ()}

    barcodes: Optional[list[str]] = Field(
        None, description="Все штрихкоды товара."
    )
    color_image: Optional[list[str]] = Field(
        None, description="URL маркетингового цвета."
    )
    commissions: Optional[list[ProductInfoListCommission]] = Field(
        None, description="Применяемые комиссии."
    )
    created_at: datetime.datetime = Field(
        ..., description="Дата и время создания товара."
    )
    currency_code: Optional[str] = Field(
        None, description="Код валюты."
    )
    description_category_id: Optional[int] = Field(
        None, description="Идентификатор категории."
    )
    discounted_fbo_stocks: Optional[int] = Field(
        None, description="Остатки уценённого товара на складе Ozon."
    )
    errors: Optional[list[ProductInfoListError]] = Field(
        None, description="Информация об ошибках."
    )
    has_discounted_fbo_item: Optional[bool] = Field(
        None, description="Есть уцененные товары на складе Ozon."
    )
    id: int = Field(
        ..., description="Идентификатор Ozon (product_id)."
    )
    images: Optional[list[str]] = Field(
        None, description="Изображения товара."
    )
    images360: Optional[list[str]] = Field(
        None, description="Изображения товара для 360."
    )
    is_archived: bool = Field(
        ..., description="Товарная карточка в архиве."
    )
    is_autoarchived: bool = Field(
        ..., description="Товарная карточка архивируется автоматически."
    )
    is_discounted: bool = Field(
        ..., description="Товар является уцененным."
    )
    is_kgt:  bool = Field(
        ..., description="Товар является крупногабаритным."
    )
    is_prepayment_allowed: Optional[bool] = Field(
        None, description="Возможна предоплата."
    )
    is_super: bool = Field(
        ..., description="Является супер-товаром."
    )
    marketing_price: Optional[str] = Field(    # 12 ноября 2025 отключим параметр price.marketing_price в ответе метода.
        None, description="Цена на товар с учетом акций (значение указано на витрине)."
    )
    min_price: Optional[str] = Field(
        None, description="Минимальная цена товара при бустинге."
    )
    model_info: ProductInfoListModelInfo = Field(
        ..., description="Информация о модели товара."
    )
    name: str = Field(
        ..., description="Наименование товара."
    )
    offer_id: str = Field(
        ..., description="Идентификатор товара в системе продавца."
    )
    old_price: Optional[str] = Field(
        None, description="Цена до учёта скидок (на карточке товара отображается зачёркнутой)."
    )
    price: Optional[str] = Field(
        None, description="Текущая цена товара."
    )
    price_indexes: ProductInfoListPriceIndexes = Field(
        ..., description="Ценовые индексы товара."
    )
    primary_image: Optional[list[str]] = Field(
        None, description="Главное изображение (если не указано, то по индексам)."
    )
    sources: list[ProductInfoListSource] = Field(
        default_factory=list, description="Информация об источниках схожих предложений."
    )
    statuses: ProductInfoListStatuses = Field(
        ..., description="Описание состояний товара на Ozon."
    )
    stocks: ProductInfoListStocks = Field(
        ..., description="Информация об остатках товара."
    )
    type_id: Optional[int] = Field(
        None, description="Идентификатор типа товара."
    )
    updated_at: datetime.datetime = Field(
        ..., description="Дата и время обновления информации."
    )
    vat: Optional[VAT | str] = Field(
        None, description="Ставка НДС."
    )
    visibility_details: ProductInfoListVisibilityDetails = Field(
        ..., description="Настройки видимости товара."
    )
    volume_weight: Optional[float] = Field(
        None, description="Объемный вес товара."
    )


class ProductInfoListResponse(BaseModel):
    """Описывает схему ответа на запрос получения информации о товарах по их идентификаторам.

    Attributes:
        items: Массив данных о товарах
    """
    items: list[ProductInfoListItem] = Field(
        default_factory=list, description="Массив данных о товарах."
    )
