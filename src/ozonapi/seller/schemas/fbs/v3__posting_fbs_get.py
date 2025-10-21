"""https://docs.ozon.ru/api/seller/#operation/PostingAPI_GetFbsPostingV3"""
from typing import Optional

from pydantic import BaseModel, Field

from . import PostingFBSPosting
from .entities import PostingFBSFilterWith
from ...common.enumerations.localization import CurrencyCode
from ...common.enumerations.postings import PostingSubstatus, PrrOption


class PostingFBSGetRequestWith(PostingFBSFilterWith):
    """Дополнительные поля, которые нужно добавить в ответ.

    Attributes:
        analytics_data: Добавить в ответ данные аналитики (опционально)
        barcodes: Добавить в ответ штрихкоды отправления (опционально)
        financial_data: Добавить в ответ финансовые данные (опционально)
        legal_info: Добавить в ответ юридическую информацию (опционально)
        product_exemplars: Добавить в ответ данные о продуктах и их экземплярах (опционально)
        related_postings: Добавить в ответ номера связанных отправлений. Связанные отправления — те, на которое было разделено родительское отправление при сборке
        translit: Выполнить транслитерацию возвращаемых значений (опционально)
    """
    product_exemplars: Optional[bool] = Field(
        False, description="Добавить в ответ данные о продуктах и их экземплярах."
    )
    related_postings: Optional[bool] = Field(
        False, description="Добавить в ответ номера связанных отправлений. Связанные отправления — те, на которое было разделено родительское отправление при сборке."
    )


class PostingFBSGetRequest(BaseModel):
    """Описывает схему запроса.

    Attributes:
        posting_number: Идентификатор отправления
        with_: Дополнительные поля, которые нужно добавить в ответ
    """
    model_config = {'populate_by_name': True}

    posting_number: str = Field(
        ..., description="Идентификатор отправления."
    )
    with_: Optional[PostingFBSGetRequestWith] = Field(
        None, description="Дополнительные поля, которые нужно добавить в ответ.",
        alias="with",
    )


class PostingFBSGetResultAdditionalData(BaseModel):
    """Дополнительная информация об отправлении

    Attributes:
        key: ключ
        value: значение
    """
    key: Optional[str] = Field(None)
    value: Optional[str] = Field(None)


class PostingFBSGetResultCourier(BaseModel):
    """Данные о курьере.
    Attributes:
        car_model: Модель автомобиля
        car_number: Номер автомобиля
        name: Полное имя курьера
        phone: Телефон курьера (всегда возвращает пустую строку)
    """
    car_model: Optional[str] = Field(
        None, description="Модель автомобиля."
    )
    car_number: Optional[str] = Field(
        None, description="Номер автомобиля."
    )
    name: Optional[str] = Field(
        None, description="Полное имя курьера."
    )
    phone: Optional[str] = Field(
        None, description="Телефон курьера (всегда возвращает пустую строку)."
    )


class PostingFBSGetResultProductExemplarsProductExemplar(BaseModel):
    """Детализированная информация об экземпляре продукта.

    Attributes:
        exemplar_id: Идентификатор экземпляра
        mandatory_mark: Обязательная маркировка «Честный ЗНАК»
        gtd: Номер грузовой таможенной декларации (ГТД)
        is_gtd_absent: Признак того, что не указан номер таможенной декларации
        rnpt: Регистрационный номер партии товара (РНПТ)
        is_rnpt_absent: Признак того, что не указан регистрационный номер партии товара (РНПТ)
        weight: Фактический вес экземпляра
        imei: Список IMEI мобильных устройств
    """
    exemplar_id: Optional[int] = Field(
        None, description="Идентификатор экземпляра."
    )
    mandatory_mark: Optional[str] = Field(
        None, description="Обязательная маркировка «Честный ЗНАК»."
    )
    gtd: Optional[str] = Field(
        None, description="Номер грузовой таможенной декларации (ГТД)."
    )
    is_gtd_absent: Optional[bool] = Field(
        None, description="Признак того, что не указан номер таможенной декларации."
    )
    rnpt: Optional[str] = Field(
        None, description="Регистрационный номер партии товара (РНПТ)."
    )
    is_rnpt_absent: Optional[bool] = Field(
        None, description="Признак того, что не указан регистрационный номер партии товара (РНПТ)."
    )
    weight: Optional[float] = Field(
        None, description="Фактический вес экземпляра."
    )
    imei: Optional[list[str]] = Field(
        None, description="Список IMEI мобильных устройств."
    )


class PostingFBSGetResultProductExemplarsProduct(BaseModel):
    """Информация об экземпляре продукта.

    Attributes:
        exemplars: Информация по экземплярам
        sku: Идентификатор товара в системе Ozon — SKU
    """
    exemplars: Optional[list[PostingFBSGetResultProductExemplarsProductExemplar]] = Field(
        default_factory=list, description="Информация по экземплярам."
    )
    sku: int = Field(
        ..., description="Идентификатор товара в системе Ozon — SKU."
    )


class PostingFBSGetResultProductExemplars(BaseModel):
    """Информация по продуктам и их экземплярам.
    Ответ содержит поле product_exemplars, если в запросе передан признак with.product_exemplars = true.

    Attributes:
        products: Информация по продуктам
    """
    products: Optional[list[PostingFBSGetResultProductExemplarsProduct]] = Field(
        default_factory=list, description="Информация по продуктам."
    )


class PostingFBSGetResultRelatedPostings(BaseModel):
    """Связанные отправления.

    Attributes:
        related_posting_numbers: Список номеров связанных отправлений
    """
    related_posting_numbers: Optional[list[str]] = Field(
        default_factory=list, description="Список номеров связанных отправлений."
    )


class PostingFBSGetResultPrrOption(BaseModel):
    """Информация об услуге погрузочно-разгрузочных работ.
    Актуально для КГТ-отправлений с доставкой силами продавца или интегрированной службой.

    Attributes:
        code: Код услуги погрузочно-разгрузочных работ
        price: Стоимость услуги, которую Ozon компенсирует продавцу
        currency_code: Валюта
        floor: Этаж, на который нужно поднять товар
    """
    code: Optional[PrrOption] = Field(
        None, description="Код услуги погрузочно-разгрузочных работ."
    )
    price: Optional[str] = Field(
        None, description="Стоимость услуги, которую Ozon компенсирует продавцу."
    )
    currency_code: Optional[CurrencyCode] = Field(
        None, description="Валюта."
    )
    floor: Optional[str] = Field(
        None, description="Этаж, на который нужно поднять товар."
    )


class PostingFBSGetResult(PostingFBSPosting):
    """Детализированная информация об отправлении.

    Attributes:
        additional_data: Дополнительная информация
        addressee: Контактные данные получателя
        analytics_data: Данные аналитики
        available_actions: Доступные действия
        barcodes: Штрихкоды отправления
        cancellation: Информация об отмене
        courier: Данные о курьере
        customer: Данные о покупателе
        delivering_date: Дата передачи отправления в доставку
        delivery_method: Метод доставки
        delivery_price: Стоимость доставки
        financial_data: Данные о стоимости товара
        in_process_at: Дата и время начала обработки отправления
        is_express: Признак быстрой доставки Ozon Express
        is_multibox: Признак многокоробочного товара
        legal_info: Юридическая информация о покупателе
        multi_box_qty: Количество коробок
        optional: Список товаров с дополнительными характеристиками
        order_id: Идентификатор заказа
        order_number: Номер заказа
        parent_posting_number: Номер родительского отправления
        pickup_code_verified_at: Дата успешной валидации кода курьера
        posting_number: Номер отправления
        product_exemplars: Информация по продуктам и их экземплярам (ответ содержит поле product_exemplars, если в запросе передан признак with_.product_exemplars = true)
        products: Список товаров в отправлении
        provider_status: Статус службы доставки
        prr_option: Информация об услуге погрузочно-разгрузочных работ
        related_postings: Связанные отправления
        related_weight_postings: Список номеров связанных весовых отправлений
        quantum_id: Идентификатор эконом-товара
        requirements: Требования к товарам
        shipment_date: Дата и время, до которой необходимо собрать отправление. Показываем рекомендованное время отгрузки. По истечении этого времени начнёт применяться новый тариф, информацию о нём уточняйте в поле tariffication.
        shipment_date_without_delay: Дата и время отгрузки без просрочки
        status: Статус отправления
        substatus: Подстатус отправления
        previous_substatus: Предыдущий подстатус отправления
        tpl_integration_type: Тип интеграции со службой доставки
        tracking_number: Трек-номер отправления
        tariffication: Информация по тарификации отгрузки
    """
    additional_data: Optional[list[PostingFBSGetResultAdditionalData]] = Field(
        default_factory=list, description="Дополнительная информация."
    )
    courier: Optional[PostingFBSGetResultCourier] = Field(
        None, description="Данные о курьере."
    )
    delivery_price: Optional[str] = Field(
        None, description="Стоимость доставки."
    )
    product_exemplars: Optional[PostingFBSGetResultProductExemplars] = Field(
        None, description="Информация по продуктам и их экземплярам. Ответ содержит поле product_exemplars, если в запросе передан признак with.product_exemplars = true."
    )
    provider_status: Optional[str] = Field(
        None, description="Статус службы доставки."
    )
    prr_option: Optional[PostingFBSGetResultPrrOption] = Field(
        None, description="Информация об услуге погрузочно-разгрузочных работ. Актуально для КГТ-отправлений с доставкой силами продавца или интегрированной службой."
    )
    related_postings: Optional[PostingFBSGetResultRelatedPostings] = Field(
        None, description="Связанные отправления."
    )
    related_weight_postings: Optional[list[str]] = Field(
        default_factory=list, description="Список номеров связанных весовых отправлений."
    )
    previous_substatus: Optional[PostingSubstatus] = Field(
        None, description="Предыдущий подстатус отправления."
    )


class PostingFBSGetResponse(BaseModel):
    """Информация об отправлении.

    Attributes:
        result: Информация об отправлении
    """
    result: PostingFBSGetResult = Field(
        ..., description="Детализированная информация об отправлении."
    )