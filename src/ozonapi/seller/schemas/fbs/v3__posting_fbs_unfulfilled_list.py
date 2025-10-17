"""https://docs.ozon.ru/api/seller/#operation/PostingAPI_GetFbsPostingUnfulfilledList"""
import datetime
from typing import Optional, Any

from pydantic import BaseModel, Field, field_validator, model_validator

from ...common.enumerations.localization import CurrencyCode
from ...common.enumerations.postings import AvailablePostingActions, PostingStatus, PostingSubstatus, \
    CancellationType, PrrOption, TplIntegrationType
from ...common.enumerations.requests import SortingDirection
from ..base import BaseRequestOffset, BaseAddressee, BaseDeliveryMethod


class PostingFBSUnfulfilledListRequestFilterLastChangedStatusDate(BaseModel):
    """Период, в который последний раз изменялся статус у отправлений.

    Attributes:
        from_: Дата начала периода
        to_: Дата окончания периода
    """
    from_: datetime.datetime = Field(
        ...,
        description="Дата начала периода.",
        alias="from"
    )
    to_: datetime.datetime = Field(
        ...,
        description="Дата окончания периода.",
        alias="to"
    )


class PostingFBSUnfulfilledListFilterWith(BaseModel):
    """Дополнительные поля, которые нужно добавить в ответ.

    Attributes:
        analytics_data: Добавить в ответ данные аналитики (опционально)
        barcodes: Добавить в ответ штрихкоды отправления (опционально)
        financial_data: Добавить в ответ финансовые данные (опционально)
        legal_info: Добавить в ответ юридическую информацию (опционально)
        translit: Выполнить транслитерацию возвращаемых значений (опционально)
    """
    analytics_data: Optional[bool] = Field(
        False, description="Добавить в ответ данные аналитики."
    )
    barcodes: Optional[bool] = Field(
        False, description="Добавить в ответ штрихкоды отправления."
    )
    financial_data: Optional[bool] = Field(
        False, description="Добавить в ответ финансовые данные."
    )
    legal_info: Optional[bool] = Field(
        False, description="Добавить в ответ юридическую информацию."
    )
    translit: Optional[bool] = Field(
        False, description="Выполнить транслитерацию возвращаемых значений."
    )


class PostingFBSUnfulfilledListFilter(BaseModel):
    """Фильтр запроса на получение информации о необработанных отправлениях FBS и rFBS
    за указанный период времени (максимум 1 год).

    Используйте фильтр либо по времени сборки — cutoff, либо по дате передачи отправления в доставку — delivering_date.
    Если использовать их вместе, в ответе вернётся ошибка.

    Чтобы использовать фильтр по времени сборки, заполните поля cutoff_from и cutoff_to.

    Чтобы использовать фильтр по дате передачи отправления в доставку,
    заполните поля delivering_date_from и delivering_date_to.

    Attributes:
        cutoff_from: Начало периода до которого продавцу нужно собрать заказ (опционально)
        cutoff_to: Конец периода до которого продавцу нужно собрать заказ (опционально)
        delivering_date_from: Минимальная дата передачи отправления в доставку (опционально)
        delivering_date_to: Максимальная дата передачи отправления в доставку (опционально)
        delivery_method_id: Список идентификаторов способов доставки (опционально, можно получить с помощью метода delivery_method_list())
        is_quantum: true, чтобы получить только отправления квантов, false - все отправления (опционально)
        provider_id: Идентификатор службы доставки (опционально, можно получить с помощью метода delivery_method_list())
        status: Статус отправления (опционально)
        warehouse_id: Идентификатор склада (опционально, можно получить с помощью метода warehouse_list())
        last_changed_status_date: Период, в который последний раз изменялся статус у отправлений (опционально)
    """
    cutoff_from: Optional[datetime.datetime | str] = Field(
        None, description="Фильтр по времени, до которого продавцу нужно собрать заказ. Начало периода."
    )
    cutoff_to: Optional[datetime.datetime | str] = Field(
        None, description="Фильтр по времени, до которого продавцу нужно собрать заказ. Конец периода."
    )
    delivering_date_from: Optional[datetime.datetime | str] = Field(
        None, description="Минимальная дата передачи отправления в доставку."
    )
    delivering_date_to: Optional[datetime.datetime | str] = Field(
        None, description="Максимальная дата передачи отправления в доставку."
    )
    delivery_method_id: Optional[list[int]] = Field(
        default_factory=list, description="Идентификаторы способов доставки. Можно получить с помощью метода delivery_method_list()."
    )
    is_quantum: Optional[bool] = Field(
        False, description="true, чтобы получить только отправления квантов. false - все отправления."
    )
    provider_id: Optional[list[int]] = Field(
        default_factory=list, description="Идентификатор службы доставки. Можно получить с помощью метода delivery_method_list()."
    )
    status: Optional[PostingStatus] = Field(
        None, description="Статус отправления."
    )
    warehouse_id: Optional[list[int]] = Field(
        default_factory=list, description="Идентификатор склада. Можно получить с помощью метода warehouse_list()."
    )
    last_changed_status_date: Optional[PostingFBSUnfulfilledListRequestFilterLastChangedStatusDate] = Field(
        None, description="Период, в который последний раз изменялся статус у отправлений."
    )

    @field_validator(
        'cutoff_from', 'cutoff_to', 'delivering_date_from', 'delivering_date_to',
        mode='after'
    )
    def serialize_datetime(cls, value):
        """Сериализует значение datetime.datetime в строку"""
        if isinstance(value, datetime.datetime):
            if value.tzinfo is None:
                value = value.replace(tzinfo=datetime.timezone.utc)

            utc_dt = value.astimezone(datetime.timezone.utc)

            return utc_dt.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
        return value

    @model_validator(mode='after')
    def validate_exclusive_filters(self) -> 'PostingFBSUnfulfilledListFilter':
        cutoff_filled = self.cutoff_from is not None or self.cutoff_to is not None

        delivering_date_filled = self.delivering_date_from is not None or self.delivering_date_to is not None

        if cutoff_filled and delivering_date_filled:
            raise ValueError(
                "Нельзя использовать одновременно фильтры cutoff и delivering_date. "
            )

        if not cutoff_filled and not delivering_date_filled:
            raise ValueError(
                "Должен быть использован один из фильтров: либо cutoff, либо delivering_date."
            )

        return self


class PostingFBSUnfulfilledListRequest(BaseRequestOffset):
    """Описывает схему запроса на получение информации о необработанных отправлениях FBS и rFBS
    за указанный период времени (максимум 1 год).

    Attributes:
        dir: Направление сортировки (опционально)
        filter: Фильтр выборки (опционально)
        limit: Количество значений в ответе (опционально, максимум 1000)
        offset (int): Количество элементов, которое будет пропущено в ответе (опционально)
        with_: Дополнительные поля, которые нужно добавить в ответ (опционально)
    """
    dir: Optional[SortingDirection] = Field(
        SortingDirection.ASC, description="Направление сортировки."
    )
    filter: PostingFBSUnfulfilledListFilter = Field(
        ..., description="Фильтр запроса. Используйте фильтр либо cutoff, либо delivering_date. Иначе будет ошибка."
    )
    limit: Optional[int] = Field(
        1000, description="Количество значений в ответе.",
        ge=1, le=1000,
    )
    with_: Optional[PostingFBSUnfulfilledListFilterWith] = Field(
        None, description="Дополнительные поля, которые нужно добавить в ответ.",
        alias="with",
    )


class PostingFBSUnfulfilledListAddressee(BaseAddressee):
    """Контактные данные получателя.

    Attributes:
        name (str | None): Имя покупателя
        phone (str | None): Всегда возвращает пустую строку (для получения подменного номера метод posting_fbs_get())
    """
    pass


class PostingFBSUnfulfilledListAnalyticsData(BaseModel):
    """Данные аналитики.

    Attributes:
        city: Город доставки
        delivery_date_begin: Дата и время начала доставки
        delivery_date_end: Дата и время конца доставки
        delivery_type: Способ доставки
        is_legal: Признак юридического лица
        is_premium: Наличие подписки Premium
        payment_type_group_name: Способ оплаты
        region: Регион доставки
        tpl_provider: Служба доставки
        tpl_provider_id: Идентификатор службы доставки
        warehouse: Название склада отправки заказа
        warehouse_id: Идентификатор склада
    """
    city: Optional[str] = Field(
        ..., description="Город доставки. Только для отправлений rFBS и продавцов из СНГ."
    )
    delivery_date_begin: Optional[datetime.datetime] = Field(
        None, description="Дата и время начала доставки."
    )
    delivery_date_end: Optional[datetime.datetime] = Field(
        None, description="Дата и время конца доставки."
    )
    delivery_type: str = Field(
        None, description="Способ доставки."
    )
    is_legal: bool = Field(
        ..., description="Признак, что получатель юридическое лицо."
    )
    is_premium: bool = Field(
        ..., description="Наличие подписки Premium."
    )
    payment_type_group_name: str = Field(
        ..., description="Способ оплаты."
    )
    region: Optional[str] = Field(
        ..., description="Регион доставки. Только для отправлений rFBS."
    )
    tpl_provider: str = Field(
        ..., description="Служба доставки."
    )
    tpl_provider_id: int = Field(
        ..., description="Идентификатор службы доставки."
    )
    warehouse: str = Field(
        ..., description="Название склада отправки заказа."
    )
    warehouse_id: int = Field(
        ..., description="Идентификатор склада."
    )


class PostingFBSUnfulfilledListBarcodes(BaseModel):
    """Штрихкоды отправления.

    Attributes:
        lower_barcode: Нижний штрихкод на маркировке отправления
        upper_barcode: Верхний штрихкод на маркировке отправления
    """
    lower_barcode: str = Field(
        ..., description="Нижний штрихкод на маркировке отправления."
    )
    upper_barcode: str = Field(
        ..., description="Верхний штрихкод на маркировке отправления."
    )


class PostingFBSUnfulfilledListCancellation(BaseModel):
    """Информация об отмене.

    Attributes:
        affect_cancellation_rating: Влияние отмены на рейтинг продавца
        cancel_reason: Причина отмены
        cancel_reason_id: Идентификатор причины отмены отправления
        cancellation_initiator: Инициатор отмены
        cancellation_type: Тип отмены отправления
        cancelled_after_ship: Признак отмены после сборки отправления
    """
    affect_cancellation_rating: bool = Field(
        ..., description="Если отмена влияет на рейтинг продавца — true."
    )
    cancel_reason: str = Field(
        ..., description="Причина отмены."
    )
    cancel_reason_id: int = Field(
        ..., description="Идентификатор причины отмены отправления."
    )
    cancellation_initiator: str = Field(
        ..., description="Инициатор отмены."
    )
    cancellation_type: CancellationType = Field(
        ..., description="Тип отмены отправления."
    )
    cancelled_after_ship: bool = Field(
        ..., description="Если отмена произошла после сборки отправления — true."
    )


class PostingFBSUnfulfilledListCustomerAddress(BaseModel):
    """Информация об адресе доставки.

    Attributes:
        address_tail: Адрес в текстовом формате
        city: Город доставки
        comment: Комментарий к заказу
        country: Страна доставки
        district: Район доставки
        latitude: Широта
        longitude: Долгота
        provider_pvz_code: Код пункта выдачи заказов 3PL провайдера
        pvz_code: Код пункта выдачи заказов
        region: Регион доставки
        zip_code: Почтовый индекс получателя
    """
    address_tail: Optional[str] = Field(
        None, description="Адрес в текстовом формате."
    )
    city: Optional[str] = Field(
        None, description="Город доставки."
    )
    comment: Optional[str] = Field(
        None, description="Комментарий к заказу."
    )
    country: Optional[str] = Field(
        None, description="Страна доставки."
    )
    district: Optional[str] = Field(
        None, description="Район доставки."
    )
    latitude: Optional[float] = Field(
        None, description="Широта."
    )
    longitude: Optional[float] = Field(
        None, description="Долгота."
    )
    provider_pvz_code: Optional[str] = Field(
        None, description="Код пункта выдачи заказов 3PL провайдера."
    )
    pvz_code: Optional[int] = Field(
        None, description="Код пункта выдачи заказов."
    )
    region: Optional[str] = Field(
        None, description="Регион доставки."
    )
    zip_code: Optional[str] = Field(
        None, description="Почтовый индекс получателя."
    )


class PostingFBSUnfulfilledListCustomer(BaseAddressee):
    """
    Данные о покупателе.

    Attributes:
        address: Информация об адресе доставки
        customer_id: Идентификатор покупателя
        name (str | None): Имя покупателя
        phone (str | None): Всегда возвращает пустую строку (получить подменный номер телефона posting_fbs_get())
    """
    address: PostingFBSUnfulfilledListCustomerAddress = Field(
        ..., description="Информация об адресе доставки."
    )
    customer_id: int = Field(
        ..., description="Идентификатор покупателя."
    )


class PostingFBSUnfulfilledListDeliveryMethod(BaseDeliveryMethod):
    """Метод доставки.

    Attributes:
        tpl_provider: Служба доставки
        tpl_provider_id: Идентификатор службы доставки
        warehouse: Название склада
    """
    tpl_provider: str = Field(
        ..., description="Служба доставки."
    )
    tpl_provider_id: int = Field(
        ..., description="Идентификатор службы доставки."
    )
    warehouse: str = Field(
        ..., description="Название склада."
    )


class PostingFBSUnfulfilledListFinancialDataProducts(BaseModel):
    """Список товаров в заказе.

    Attributes:
        actions: Список акций
        currency_code: Валюта цен
        commission_amount: Размер комиссии за товар
        commission_percent: Процент комиссии
        commissions_currency_code: Код валюты комиссий
        old_price: Цена до учёта скидок
        payout: Выплата продавцу
        price: Цена товара с учётом акций
        customer_price: Цена товара для покупателя
        product_id: Идентификатор товара в системе продавца
        quantity: Количество товара в отправлении
        total_discount_percent: Процент скидки
        total_discount_value: Сумма скидки
    """
    actions: list[str] = Field(
        ..., description="Список акций."
    )
    currency_code: CurrencyCode = Field(
        ..., description="Валюта ваших цен. Cовпадает с валютой, которая установлена в настройках личного кабинета."
    )
    commission_amount: float = Field(
        ..., description="Размер комиссии за товар."
    )
    commission_percent: float = Field(
        ..., description="Процент комиссии."
    )
    commissions_currency_code: CurrencyCode = Field(
        ..., description="Код валюты, в которой рассчитывались комиссии."
    )
    old_price: float = Field(
        ..., description="Цена до учёта скидок. На карточке товара отображается зачёркнутой."
    )
    payout: float = Field(
        ..., description="Выплата продавцу."
    )
    price: float = Field(
        ..., description="Цена товара с учётом акций, кроме акций за счёт Ozon."
    )
    customer_price: float = Field(
        ..., description="Цена товара для покупателя с учётом скидок продавца и Ozon."
    )
    product_id: int = Field(
        ..., description="Идентификатор товара в системе продавца."
    )
    quantity: int = Field(
        ..., description="Количество товара в отправлении."
    )
    total_discount_percent: float = Field(
        ..., description="Процент скидки."
    )
    total_discount_value: float = Field(
        ..., description="Сумма скидки."
    )


class PostingFBSUnfulfilledListFinancialData(BaseModel):
    """Данные о стоимости товара, размере скидки, выплате и комиссии.

    Attributes:
        cluster_from: Код региона отправки заказа
        cluster_to: Код региона доставки заказа
        products: Список товаров в заказе
    """
    cluster_from: str = Field(
        ..., description="Код региона, откуда отправляется заказ."
    )
    cluster_to: str = Field(
        ..., description="Код региона, куда доставляется заказ."
    )
    products: list[PostingFBSUnfulfilledListFinancialDataProducts] = Field(
        ..., description="Список товаров в заказе."
    )


class PostingFBSUnfulfilledListLegalInfo(BaseModel):
    """Юридическая информация о покупателе.

    Attributes:
        company_name: Название компании
        inn: ИНН
        kpp: КПП
    """
    company_name: str = Field(
        ..., description="Название компании."
    )
    inn: str = Field(
        ..., description="ИНН."
    )
    kpp: str = Field(
        ..., description="КПП."
    )


class PostingFBSUnfulfilledListOptional(BaseModel):
    """Список товаров с дополнительными характеристиками.

    Attributes:
        products_with_possible_mandatory_mark: Список товаров с возможной маркировкой
    """
    products_with_possible_mandatory_mark: list[Any] = Field(
        ..., description="Список товаров с возможной маркировкой."
    )


class PostingFBSUnfulfilledListProducts(BaseModel):
    """Список товаров в отправлении.

    Attributes:
        name: Название товара
        offer_id: Идентификатор товара в системе продавца
        price: Цена товара
        quantity: Количество товара в отправлении
        sku: Идентификатор товара в системе Ozon
        currency_code: Валюта цен
        is_blr_traceable: Признак прослеживаемости товара
        is_marketplace_buyout: Признак выкупа товара в ЕАЭС и другие страны
        imei: Список IMEI мобильных устройств
    """
    name: str = Field(
        ..., description="Название товара."
    )
    offer_id: str = Field(
        ..., description="Идентификатор товара в системе продавца — артикул."
    )
    price: float = Field(
        ..., description="Цена товара."
    )
    quantity: int = Field(
        ..., description="Количество товара в отправлении."
    )
    sku: int = Field(
        ..., description="Идентификатор товара в системе Ozon — SKU."
    )
    currency_code: CurrencyCode = Field(
        ..., description="Валюта ваших цен. Совпадает с валютой, которая установлена в настройках личного кабинета."
    )
    is_blr_traceable: bool = Field(
        ..., description="Признак прослеживаемости товара."
    )
    is_marketplace_buyout: bool = Field(
        ..., description="Признак выкупа товара в ЕАЭС и другие страны."
    )
    imei: Optional[list[str]] = Field(
        None, description="Список IMEI мобильных устройств."
    )


class PostingFBSUnfulfilledListRequirements(BaseModel):
    """Список продуктов, для которых нужно передать страну-изготовителя, номер грузовой таможенной декларации (ГТД),
    регистрационный номер партии товара (РНПТ), маркировку «Честный ЗНАК», другие маркировки или вес,
    чтобы перевести отправление в следующий статус.

    Attributes:
        products_requiring_change_country: Список SKU для изменения страны-изготовителя
        products_requiring_gtd: Список SKU для передачи номеров ГТД
        products_requiring_country: Список SKU для передачи информации о стране-изготовителе
        products_requiring_mandatory_mark: Список SKU для передачи маркировки «Честный ЗНАК»
        products_requiring_jw_uin: Список товаров для передачи УИН ювелирного изделия
        products_requiring_rnpt: Список SKU для передачи РНПТ
        products_requiring_weight: Список товаров для передачи веса
        products_requiring_imei: Список идентификаторов товаров для передачи IMEI
    """
    products_requiring_change_country: list[int] = Field(
        default_factory=list, description="Список идентификаторов товаров (SKU), для которых нужно изменить страну-изготовитель."
    )
    products_requiring_gtd: list[int] = Field(
        default_factory=list, description="Список идентификаторов товаров (SKU), для которых нужно передать номера таможенной декларации (ГТД)."
    )
    products_requiring_country: list[int] = Field(
        default_factory=list, description="Список идентификаторов товаров (SKU), для которых нужно передать информацию о стране-изготовителе."
    )
    products_requiring_mandatory_mark: list[int] = Field(
        default_factory=list, description="Список идентификаторов товаров (SKU), для которых нужно передать маркировку «Честный ЗНАК»."
    )
    products_requiring_jw_uin: list[int] = Field(
        default_factory=list, description="Список товаров, для которых нужно передать уникальный идентификационный номер (УИН) ювелирного изделия."
    )
    products_requiring_rnpt: list[int] = Field(
        default_factory=list, description="Список идентификаторов товаров (SKU), для которых нужно передать регистрационный номер партии товара (РНПТ)."
    )
    products_requiring_weight: list[int] = Field(
        default_factory=list, description="Список товаров, для которых нужно передать вес."
    )
    products_requiring_imei: list[int] = Field(
        default_factory=list, description="Список идентификаторов товаров, для которых нужно передать IMEI."
    )


class PostingFBSUnfulfilledListTariffication(BaseModel):
    """Информация по тарификации отгрузки.

    Attributes:
        current_tariff_rate: Текущий процент тарификации
        current_tariff_type: Текущий тип тарификации
        current_tariff_charge: Текущая сумма скидки или надбавки
        current_tariff_charge_currency_code: Валюта суммы
        next_tariff_rate: Процент следующего тарифа
        next_tariff_type: Тип следующего тарифа
        next_tariff_charge: Сумма следующего тарифа
        next_tariff_starts_at: Дата начала нового тарифа
        next_tariff_charge_currency_code: Валюта нового тарифа
    """
    current_tariff_rate: float = Field(
        ..., description="Текущий процент тарификации."
    )
    current_tariff_type: str = Field(
        ..., description="Текущий тип тарификации — скидка или надбавка."
    )
    current_tariff_charge: str = Field(
        ..., description="Текущая сумма скидки или надбавки."
    )
    current_tariff_charge_currency_code: str = Field(
        ..., description="Валюта суммы."
    )
    next_tariff_rate: float = Field(
        ..., description="Процент, по которому будет тарифицироваться отправление через указанное в параметре next_tariff_starts_at время."
    )
    next_tariff_type: str = Field(
        ..., description="Тип тарифа, по которому будет тарифицироваться отправление через указанное в параметре next_tariff_starts_at время — скидка или надбавка."
    )
    next_tariff_charge: str = Field(
        ..., description="Сумма скидки или надбавки на следующем шаге тарификации."
    )
    next_tariff_starts_at: Optional[datetime.datetime] = Field(
        None, description="Дата и время, когда начнёт применяться новый тариф."
    )
    next_tariff_charge_currency_code: str = Field(
        ..., description="Валюта нового тарифа."
    )


class PostingFBSUnfulfilledListItem(BaseModel):
    """Информация об отправлении.

    Attributes:
        addressee: Контактные данные получателя
        analytics_data: Данные аналитики
        available_actions: Доступные действия
        barcodes: Штрихкоды отправления
        cancellation: Информация об отмене
        customer: Данные о покупателе
        delivering_date: Дата передачи отправления в доставку
        delivery_method: Метод доставки
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
        products: Список товаров в отправлении
        prr_option: Код услуги погрузочно-разгрузочных работ
        quantum_id: Идентификатор эконом-товара
        requirements: Требования к товарам
        shipment_date: Дата сборки отправления
        status: Статус отправления
        substatus: Подстатус отправления
        tpl_integration_type: Тип интеграции со службой доставки
        tracking_number: Трек-номер отправления
        tariffication: Информация по тарификации отгрузки
    """
    addressee: Optional[PostingFBSUnfulfilledListAddressee] = Field(
        None, description="Контактные данные получателя.",
    )
    analytics_data: Optional[PostingFBSUnfulfilledListAnalyticsData] = Field(
        None, description="Данные аналитики."
    )
    available_actions: list[AvailablePostingActions] = Field(
        ..., description="Доступные действия и информация об отправлении."
    )
    barcodes: Optional[PostingFBSUnfulfilledListBarcodes] = Field(
        None, description="Штрихкоды отправления."
    )
    cancellation: Optional[PostingFBSUnfulfilledListCancellation] = Field(
        None, description="Информация об отмене."
    )
    customer: Optional[PostingFBSUnfulfilledListCustomer] = Field(
        None, description="Данные о покупателе."
    )
    delivering_date: datetime.datetime = Field(
        ..., description="Дата передачи отправления в доставку."
    )
    delivery_method: PostingFBSUnfulfilledListDeliveryMethod = Field(
        ..., description="Метод доставки."
    )
    financial_data: Optional[PostingFBSUnfulfilledListFinancialData] = Field(
        None, description="Данные о стоимости товара, размере скидки, выплате и комиссии."
    )
    in_process_at: datetime.datetime = Field(
        ..., description="Дата и время начала обработки отправления."
    )
    is_express: bool = Field(
        ..., description="Если использовалась быстрая доставка Ozon Express — true."
    )
    is_multibox: bool = Field(
        ..., description="Признак, что в отправлении есть многокоробочный товар и нужно передать количество коробок."
    )
    legal_info: Optional[PostingFBSUnfulfilledListLegalInfo] = Field(
        None, description="Юридическая информация о покупателе."
    )
    multi_box_qty: Optional[int] = Field(
        None, description="Количество коробок, в которые упакован товар."
    )
    optional: Optional[PostingFBSUnfulfilledListOptional] = Field(
        None, description="Список товаров с дополнительными характеристиками."
    )
    order_id: int = Field(
        ..., description="Идентификатор заказа, к которому относится отправление."
    )
    order_number: str = Field(
        ..., description="Номер заказа, к которому относится отправление."
    )
    parent_posting_number: Optional[str] = Field(
        None, description="Номер родительского отправления, в результате разделения которого появилось текущее."
    )
    pickup_code_verified_at: Optional[datetime.datetime] = Field(
        None, description="Дата успешной валидации кода курьера. Проверить код posting_fbs_pick_up_code_verify()"
    )
    posting_number: str = Field(
        ..., description="Номер отправления."
    )
    products: list[PostingFBSUnfulfilledListProducts] = Field(
        ..., description="Список товаров в отправлении."
    )
    prr_option: Optional[PrrOption] = Field(
        None, description="Код услуги погрузочно-разгрузочных работ."
    )
    quantum_id: Optional[int] = Field(
        ..., description="Идентификатор эконом-товара."
    )
    requirements: PostingFBSUnfulfilledListRequirements = Field(
        ..., description="""
        Cписок продуктов, для которых нужно передать страну-изготовителя, номер грузовой таможенной декларации (ГТД), 
        регистрационный номер партии товара (РНПТ), маркировку «Честный ЗНАК», другие маркировки или вес, 
        чтобы перевести отправление в следующий статус.
        """
    )
    shipment_date: datetime.datetime = Field(
        ..., description="Дата и время, до которой необходимо собрать отправление."
    )
    status: PostingStatus = Field(
        ..., description="Статус отправления."
    )
    substatus: PostingSubstatus = Field(
        ..., description="Подстатус отправления."
    )
    tpl_integration_type: TplIntegrationType = Field(
        ..., description="Тип интеграции со службой доставки."
    )
    tracking_number: Optional[str] = Field(
        None, description="Трек-номер отправления."
    )
    tariffication: PostingFBSUnfulfilledListTariffication = Field(
        ..., description="Информация по тарификации отгрузки."
    )


class PostingFBSUnfulfilledListResult(BaseModel):
    """Информация о необработанных отправлениях и их количестве.

    Attributes:
        count: Счётчик элементов в ответе
        postings: Массив отправлений
    """
    count: int = Field(
        ..., description="Счётчик элементов в ответе.",
    )
    postings: Optional[list[PostingFBSUnfulfilledListItem]] = Field(
        default_factory=list, description="Массив отправлений."
    )


class PostingFBSUnfulfilledListResponse(BaseModel):
    """Описывает схему ответа на запрос информации о необработанных отправлениях FBS и rFBS.

    Attributes:
        result: Содержимое ответа
    """
    result: PostingFBSUnfulfilledListResult = Field(
        ..., description="Содержимое ответа."
    )