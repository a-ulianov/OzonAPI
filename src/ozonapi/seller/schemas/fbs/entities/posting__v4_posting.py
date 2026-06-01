from typing import Optional

from pydantic import BaseModel, Field

class PostingFBSV4Addressee(BaseModel):
    """Контактные данные получателя.

    Attributes:
        name: Имя получателя
    """
    name: Optional[str] = Field(
        None, description="Имя получателя."
    )

class PostingFBSV4AnalyticsData(BaseModel):
    """Данные аналитики.

    Attributes:
        city: Город доставки. Только для отправлений rFBS и продавцов из СНГ
        client_delivery_date_begin: Дата и время начала доставки. Только для отправлений, оформленных через [Ozon Доставку](#tag/OzonLogistics)
        client_delivery_date_end: Ожидаемая дата, до которой заказ будет доставлен. Только для отправлений, оформленных через [Ozon Доставку](#tag/OzonLogistics)
        delivery_date_begin: Дата и время начала доставки
        delivery_date_end: Дата и время конца доставки
        delivery_type: Способ доставки
        is_legal: `true`, если получатель юридическое лицо
        is_premium: `true`, если у получателя есть подписка Premium
        payment_type_group_name: Способ оплаты
        region: Регион доставки. Только для отправлений rFBS
        tpl_provider: Служба доставки
        tpl_provider_id: Идентификатор службы доставки
        warehouse: Название склада отправки заказа
        warehouse_id: Идентификатор склада
    """
    city: Optional[str] = Field(
        None, description="Город доставки. Только для отправлений rFBS и продавцов из СНГ."
    )
    client_delivery_date_begin: Optional[str] = Field(
        None, description="Дата и время начала доставки. Только для отправлений, оформленных через [Ozon Доставку](#tag/OzonLogistics)."
    )
    client_delivery_date_end: Optional[str] = Field(
        None, description="Ожидаемая дата, до которой заказ будет доставлен. Только для отправлений, оформленных через [Ozon Доставку](#tag/OzonLogistics)."
    )
    delivery_date_begin: Optional[str] = Field(
        None, description="Дата и время начала доставки."
    )
    delivery_date_end: Optional[str] = Field(
        None, description="Дата и время конца доставки."
    )
    delivery_type: Optional[str] = Field(
        None, description="Способ доставки."
    )
    is_legal: Optional[bool] = Field(
        None, description="`true`, если получатель юридическое лицо."
    )
    is_premium: Optional[bool] = Field(
        None, description="`true`, если у получателя есть подписка Premium."
    )
    payment_type_group_name: Optional[str] = Field(
        None, description="Способ оплаты."
    )
    region: Optional[str] = Field(
        None, description="Регион доставки. Только для отправлений rFBS."
    )
    tpl_provider: Optional[str] = Field(
        None, description="Служба доставки."
    )
    tpl_provider_id: Optional[int] = Field(
        None, description="Идентификатор службы доставки."
    )
    warehouse: Optional[str] = Field(
        None, description="Название склада отправки заказа."
    )
    warehouse_id: Optional[int] = Field(
        None, description="Идентификатор склада."
    )

class PostingFBSV4Barcodes(BaseModel):
    """Штрихкоды отправления.

    Attributes:
        lower_barcode: Нижний штрихкод на маркировке отправления
        upper_barcode: Верхний штрихкод на маркировке отправления
    """
    lower_barcode: Optional[str] = Field(
        None, description="Нижний штрихкод на маркировке отправления."
    )
    upper_barcode: Optional[str] = Field(
        None, description="Верхний штрихкод на маркировке отправления."
    )

class PostingFBSV4Cancellation(BaseModel):
    """Информация об отмене.

    Attributes:
        affect_cancellation_rating: `true`, если отмена влияет на рейтинг продавца
        cancel_reason: Причина отмены
        cancel_reason_id: Идентификатор причины отмены отправления
        cancellation_initiator: Инициатор отмены
        cancellation_type: Тип отмены
        cancelled_after_ship: `true`, если отмена произошла после сборки отправления
    """
    affect_cancellation_rating: Optional[bool] = Field(
        None, description="`true`, если отмена влияет на рейтинг продавца."
    )
    cancel_reason: Optional[str] = Field(
        None, description="Причина отмены."
    )
    cancel_reason_id: Optional[int] = Field(
        None, description="Идентификатор причины отмены отправления."
    )
    cancellation_initiator: Optional[str] = Field(
        None, description="Инициатор отмены."
    )
    cancellation_type: Optional[str] = Field(
        None, description="Тип отмены."
    )
    cancelled_after_ship: Optional[bool] = Field(
        None, description="`true`, если отмена произошла после сборки отправления."
    )

class PostingFBSV4Address(BaseModel):
    """Адрес доставки.

    Attributes:
        address_tail: Адрес в текстовом формате
        city: Город доставки
        comment: Комментарий к заказу
        country: Страна доставки
        district: Район доставки
        latitude: Широта
        longitude: Долгота
        provider_pvz_code: Код пункта выдачи заказов 3PL-провайдера
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
        None, description="Код пункта выдачи заказов 3PL-провайдера."
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

class PostingFBSV4Customer(BaseModel):
    """Информация о покупателе.

    Attributes:
        address: address
        customer_email: Электронная почта покупателя
        customer_id: Идентификатор покупателя
        name: Имя покупателя
        phone: Подменный контактный телефон покупателя
    """
    address: Optional[PostingFBSV4Address] = Field(
        None, description="address."
    )
    customer_email: Optional[str] = Field(
        None, description="Электронная почта покупателя."
    )
    customer_id: Optional[int] = Field(
        None, description="Идентификатор покупателя."
    )
    name: Optional[str] = Field(
        None, description="Имя покупателя."
    )
    phone: Optional[str] = Field(
        None, description="Подменный контактный телефон покупателя."
    )

class PostingFBSV4Container(BaseModel):
    """Информация о грузоместе.

    Attributes:
        cargo_type: Тип грузоместа
        container_date: Дата создания грузоместа в часовом поясе склада
        container_id: Идентификатор грузоместа
        container_number: Порядковый номер грузоместа
    """
    cargo_type: Optional[str] = Field(
        None, description="Тип грузоместа."
    )
    container_date: Optional[str] = Field(
        None, description="Дата создания грузоместа в часовом поясе склада."
    )
    container_id: Optional[int] = Field(
        None, description="Идентификатор грузоместа."
    )
    container_number: Optional[int] = Field(
        None, description="Порядковый номер грузоместа."
    )

class PostingFBSV4DeliveryMethod(BaseModel):
    """Информация о способе доставки.

    Attributes:
        id: Идентификатор способа доставки
        name: Название способа доставки
        tpl_provider: Служба доставки
        tpl_provider_id: Идентификатор службы доставки
        warehouse: Название склада
        warehouse_id: Идентификатор склада
    """
    id: Optional[int] = Field(
        None, description="Идентификатор способа доставки."
    )
    name: Optional[str] = Field(
        None, description="Название способа доставки."
    )
    tpl_provider: Optional[str] = Field(
        None, description="Служба доставки."
    )
    tpl_provider_id: Optional[int] = Field(
        None, description="Идентификатор службы доставки."
    )
    warehouse: Optional[str] = Field(
        None, description="Название склада."
    )
    warehouse_id: Optional[int] = Field(
        None, description="Идентификатор склада."
    )

class PostingFBSV4ExternalOrder(BaseModel):
    """Информация о заказе с внешней платформы.

    Attributes:
        is_external: `true`, если заказ с внешней платформы
        platform_name: Название платформы, с которой сделали заказ
    """
    is_external: Optional[bool] = Field(
        None, description="`true`, если заказ с внешней платформы."
    )
    platform_name: Optional[str] = Field(
        None, description="Название платформы, с которой сделали заказ."
    )

class PostingFBSV4Commission(BaseModel):
    """Комиссия за товар.

    Attributes:
        amount: Размер комиссии за товар
        currency: Код валюты, в которой рассчитывалась комиссия
        percent: Процент комиссии
    """
    amount: Optional[float] = Field(
        None, description="Размер комиссии за товар."
    )
    currency: Optional[str] = Field(
        None, description="Код валюты, в которой рассчитывалась комиссия."
    )
    percent: Optional[int] = Field(
        None, description="Процент комиссии."
    )

class PostingFBSV4postingMoney(BaseModel):
    """Цена товара.

    Attributes:
        amount: Сумма
        currency: Валюта
    """
    amount: Optional[str] = Field(
        None, description="Сумма."
    )
    currency: Optional[str] = Field(
        None, description="Валюта."
    )

class PostingFBSV4Products(BaseModel):
    """PostingFBSV4Products.

    Attributes:
        actions: Список акций
        commission: commission
        customer_price: customer_price
        old_price: Цена до учёта скидок. На карточке товара отображается зачёркнутой
        payout: Выплата продавцу
        price: Цена товара с учётом акций, кроме акций за счёт Ozon
        product_id: Идентификатор товара в системе Ozon — SKU
        quantity: Количество товара в отправлении
        total_discount_percent: Процент скидки
        total_discount_value: Сумма скидки
    """
    actions: Optional[list[str]] = Field(
        None, description="Список акций."
    )
    commission: Optional[PostingFBSV4Commission] = Field(
        None, description="commission."
    )
    customer_price: Optional[PostingFBSV4postingMoney] = Field(
        None, description="customer_price."
    )
    old_price: Optional[float] = Field(
        None, description="Цена до учёта скидок. На карточке товара отображается зачёркнутой."
    )
    payout: Optional[float] = Field(
        None, description="Выплата продавцу."
    )
    price: Optional[float] = Field(
        None, description="Цена товара с учётом акций, кроме акций за счёт Ozon."
    )
    product_id: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    quantity: Optional[int] = Field(
        None, description="Количество товара в отправлении."
    )
    total_discount_percent: Optional[float] = Field(
        None, description="Процент скидки."
    )
    total_discount_value: Optional[float] = Field(
        None, description="Сумма скидки."
    )

class PostingFBSV4FinancialData(BaseModel):
    """Информация о стоимости товара, размере скидки, выплате и комиссии.

    Attributes:
        cluster_from: Код региона, откуда отправляется заказ
        cluster_to: Код региона, куда доставляется заказ
        products: Список товаров в заказе
    """
    cluster_from: Optional[str] = Field(
        None, description="Код региона, откуда отправляется заказ."
    )
    cluster_to: Optional[str] = Field(
        None, description="Код региона, куда доставляется заказ."
    )
    products: Optional[list[PostingFBSV4Products]] = Field(
        None, description="Список товаров в заказе."
    )

class PostingFBSV4LegalInfo(BaseModel):
    """Юридическая информация о покупателе.

    Attributes:
        company_name: Название компании
        inn: ИНН
        kpp: КПП
    """
    company_name: Optional[str] = Field(
        None, description="Название компании."
    )
    inn: Optional[str] = Field(
        None, description="ИНН."
    )
    kpp: Optional[str] = Field(
        None, description="КПП."
    )

class PostingFBSV4Optional(BaseModel):
    """Список товаров с дополнительными характеристиками.

    Attributes:
        products_with_possible_mandatory_mark: Список товаров с возможной маркировкой
    """
    products_with_possible_mandatory_mark: Optional[list[str]] = Field(
        None, description="Список товаров с возможной маркировкой."
    )

class PostingFBSV4Products2(BaseModel):
    """PostingFBSV4Products2.

    Attributes:
        imei: Список IMEI мобильных устройств
        is_blr_traceable: `true`, если товар отслеживаемый
        is_marketplace_buyout: `true`, если Ozon выкупил товар для доставки в ЕАЭС и другие страны
        name: Название товара
        offer_id: Идентификатор товара в системе продавца — артикул
        price: price
        product_color: Цвет товара
        quantity: Количество товара в отправлении
        sku: Идентификатор товара в системе Ozon — SKU
        weight: Вес товара в упаковке
    """
    imei: Optional[list[str]] = Field(
        None, description="Список IMEI мобильных устройств."
    )
    is_blr_traceable: Optional[bool] = Field(
        None, description="`true`, если товар отслеживаемый."
    )
    is_marketplace_buyout: Optional[bool] = Field(
        None, description="`true`, если Ozon выкупил товар для доставки в ЕАЭС и другие страны."
    )
    name: Optional[str] = Field(
        None, description="Название товара."
    )
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    price: Optional[PostingFBSV4postingMoney] = Field(
        None, description="price."
    )
    product_color: Optional[str] = Field(
        None, description="Цвет товара."
    )
    quantity: Optional[int] = Field(
        None, description="Количество товара в отправлении."
    )
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    weight: Optional[float] = Field(
        None, description="Вес товара в упаковке."
    )

class PostingFBSV4Requirements(BaseModel):
    """Товары, для которых нужна дополнительная информация.

    Attributes:
        products_requiring_change_country: Список идентификаторов товаров (SKU), для которых нужно изменить страну-изготовителя. Чтобы изменить страну-изготовителя, используйте методы [/v2/posting/fbs/product/country/list](#operation/PostingAPI_ListCountryProductFbsPostingV2) и [/v2/posting/fbs/product/country/set](#operation/PostingAPI_SetCountryProductFbsPostingV2)
        products_requiring_country: Список идентификаторов товаров (SKU), для которых нужно передать информацию о стране-изготовителе
        products_requiring_gtd: Список идентификаторов товаров (SKU), для которых нужно передать номера грузовой таможенной декларации (ГТД)
        products_requiring_imei: Список идентификаторов товаров, для которых нужно передать IMEI
        products_requiring_jw_uin: Список товаров, для которых нужно передать уникальный идентификационный номер (УИН) ювелирного изделия
        products_requiring_mandatory_mark: Список идентификаторов товаров (SKU), для которых нужно передать маркировку «Честный знак»
        products_requiring_rnpt: Список идентификаторов товаров (SKU), для которых нужно передать регистрационный номер партии товара (РНПТ)
        products_requiring_weight: Список товаров, для которых нужно передать вес
    """
    products_requiring_change_country: Optional[list[str]] = Field(
        None, description="Список идентификаторов товаров (SKU), для которых нужно изменить страну-изготовителя. Чтобы изменить страну-изготовителя, используйте методы [/v2/posting/fbs/product/country/list](#operation/PostingAPI_ListCountryProductFbsPostingV2) и [/v2/posting/fbs/product/country/set](#operation/PostingAPI_SetCountryProductFbsPostingV2)."
    )
    products_requiring_country: Optional[list[str]] = Field(
        None, description="Список идентификаторов товаров (SKU), для которых нужно передать информацию о стране-изготовителе."
    )
    products_requiring_gtd: Optional[list[str]] = Field(
        None, description="Список идентификаторов товаров (SKU), для которых нужно передать номера грузовой таможенной декларации (ГТД)."
    )
    products_requiring_imei: Optional[list[str]] = Field(
        None, description="Список идентификаторов товаров, для которых нужно передать IMEI."
    )
    products_requiring_jw_uin: Optional[list[str]] = Field(
        None, description="Список товаров, для которых нужно передать уникальный идентификационный номер (УИН) ювелирного изделия."
    )
    products_requiring_mandatory_mark: Optional[list[str]] = Field(
        None, description="Список идентификаторов товаров (SKU), для которых нужно передать маркировку «Честный знак»."
    )
    products_requiring_rnpt: Optional[list[str]] = Field(
        None, description="Список идентификаторов товаров (SKU), для которых нужно передать регистрационный номер партии товара (РНПТ)."
    )
    products_requiring_weight: Optional[list[str]] = Field(
        None, description="Список товаров, для которых нужно передать вес."
    )

class PostingFBSV4Currenttariffcharge(BaseModel):
    """Скидка или надбавка.

    Attributes:
        amount: Сумма
        currency: Валюта
    """
    amount: Optional[str] = Field(
        None, description="Сумма."
    )
    currency: Optional[str] = Field(
        None, description="Валюта."
    )

class PostingFBSV4Currenttariffmincharge(BaseModel):
    """Минимальная скидка или надбавка.

    Attributes:
        amount: Сумма
        currency: Валюта
    """
    amount: Optional[str] = Field(
        None, description="Сумма."
    )
    currency: Optional[str] = Field(
        None, description="Валюта."
    )

class PostingFBSV4Nexttariffcharge(BaseModel):
    """Скидка или надбавка через время из параметра `next_tariff_starts_at`.

    Attributes:
        amount: Сумма
        currency: Валюта
    """
    amount: Optional[str] = Field(
        None, description="Сумма."
    )
    currency: Optional[str] = Field(
        None, description="Валюта."
    )

class PostingFBSV4Nexttariffmincharge(BaseModel):
    """Минимальная скидка или надбавка через время из параметра `next_tariff_starts_at`.

    Attributes:
        amount: Сумма
        currency: Валюта
    """
    amount: Optional[str] = Field(
        None, description="Сумма."
    )
    currency: Optional[str] = Field(
        None, description="Валюта."
    )

class PostingFBSV4Tariffication(BaseModel):
    """Информация по тарификации отгрузки.

    Attributes:
        current_tariff_charge: current_tariff_charge
        current_tariff_min_charge: current_tariff_min_charge
        current_tariff_rate: Процент тарификации
        current_tariff_type: Тип тарификации — скидка или надбавка
        next_tariff_charge: next_tariff_charge
        next_tariff_min_charge: next_tariff_min_charge
        next_tariff_rate: Процент, по которому будет тарифицироваться отправление через время из параметра `next_tariff_starts_at`
        next_tariff_starts_at: Дата и время, когда начнёт применяться новый тариф
        next_tariff_type: Тип тарификации через время из параметра `next_tariff_starts_at` — скидка или надбавка
    """
    current_tariff_charge: Optional[PostingFBSV4Currenttariffcharge] = Field(
        None, description="current_tariff_charge."
    )
    current_tariff_min_charge: Optional[PostingFBSV4Currenttariffmincharge] = Field(
        None, description="current_tariff_min_charge."
    )
    current_tariff_rate: Optional[float] = Field(
        None, description="Процент тарификации."
    )
    current_tariff_type: Optional[str] = Field(
        None, description="Тип тарификации — скидка или надбавка."
    )
    next_tariff_charge: Optional[PostingFBSV4Nexttariffcharge] = Field(
        None, description="next_tariff_charge."
    )
    next_tariff_min_charge: Optional[PostingFBSV4Nexttariffmincharge] = Field(
        None, description="next_tariff_min_charge."
    )
    next_tariff_rate: Optional[float] = Field(
        None, description="Процент, по которому будет тарифицироваться отправление через время из параметра `next_tariff_starts_at`."
    )
    next_tariff_starts_at: Optional[str] = Field(
        None, description="Дата и время, когда начнёт применяться новый тариф."
    )
    next_tariff_type: Optional[str] = Field(
        None, description="Тип тарификации через время из параметра `next_tariff_starts_at` — скидка или надбавка."
    )

class PostingFBSV4TarifficationStep(BaseModel):
    """PostingFBSV4TarifficationStep.

    Attributes:
        min_charge: min_charge
        tariff_charge: tariff_charge
        tariff_deadline_at: Дата и время окончания этапа тарификации. После этой даты автоматически начинается следующий этап
        tariff_rate: Процент скидки или надбавки
        tariff_type: Тип тарификации
    """
    min_charge: Optional[PostingFBSV4Currenttariffmincharge] = Field(
        None, description="min_charge."
    )
    tariff_charge: Optional[PostingFBSV4Currenttariffcharge] = Field(
        None, description="tariff_charge."
    )
    tariff_deadline_at: Optional[str] = Field(
        None, description="Дата и время окончания этапа тарификации. После этой даты автоматически начинается следующий этап."
    )
    tariff_rate: Optional[float] = Field(
        None, description="Процент скидки или надбавки."
    )
    tariff_type: Optional[str] = Field(
        None, description="Тип тарификации."
    )

class PostingFBSV4Postings(BaseModel):
    """PostingFBSV4Postings.

    Attributes:
        addressee: addressee
        analytics_data: analytics_data
        available_actions: Доступные действия и информация об отправлении
        barcodes: barcodes
        cancellation: cancellation
        customer: customer
        container: container
        container_sort_type: Тип сортировки грузоместа
        delivering_date: Дата передачи отправления в доставку
        delivery_method: delivery_method
        delivery_schema: Схема доставки
        destination_place_id: Идентификатор места назначения
        destination_place_name: Название места назначения
        external_order: external_order
        financial_data: financial_data
        in_process_at: Дата и время начала обработки отправления
        is_click_and_collect: `true`, если отправление доставляется методом «Самовывоз из магазина»
        is_express: `true`, если использовалась быстрая доставка Ozon Express
        is_multibox: Признак, что в отправлении есть многокоробочный товар и нужно передать количество коробок для него
        is_presortable: `true`, если товар — пересорт
        legal_info: legal_info
        multi_box_qty: Количество коробок, в которые упакован товар
        optional: optional
        order_id: Идентификатор заказа, к которому относится отправление
        order_number: Номер заказа, к которому относится отправление
        parent_posting_number: Номер родительского отправления, в результате разделения которого появилось текущее
        pickup_code_verified_at: Дата и время успешной валидации кода курьера. Проверьте код курьера методом [/v1/posting/fbs/pick-up-code/verify](#operation/PostingAPI_PostingFBSPickupCodeVerify)
        posting_number: Номер отправления
        products: Список товаров в отправлении
        prr_option: Код услуги погрузочно-разгрузочных работ
        quantum_id: Идентификатор эконом-товара
        require_blr_traceable_attrs: `true`, если нужно заполнить атрибуты отслеживаемости
        requirements: requirements
        shipment_date: Дата и время, до которой нужно собрать отправление. Показываем рекомендованное время отгрузки. По истечении этого времени начнёт применяться новый тариф, информацию о нём получите в поле `tariffication`
        shipment_date_without_delay: Дата и время отгрузки без просрочки
        status: Статус отправления
        substatus: Подстатус отправления
        tariffication: tariffication
        tariffication_steps: Этапы тарификации
        tpl_integration_type: Тип интеграции со службой доставки
        tracking_number: Трек-номер отправления
        volume_weight: Объёмный вес товара
    """
    addressee: Optional[PostingFBSV4Addressee] = Field(
        None, description="addressee."
    )
    analytics_data: Optional[PostingFBSV4AnalyticsData] = Field(
        None, description="analytics_data."
    )
    available_actions: Optional[list[str]] = Field(
        None, description="Доступные действия и информация об отправлении."
    )
    barcodes: Optional[PostingFBSV4Barcodes] = Field(
        None, description="barcodes."
    )
    cancellation: Optional[PostingFBSV4Cancellation] = Field(
        None, description="cancellation."
    )
    customer: Optional[PostingFBSV4Customer] = Field(
        None, description="customer."
    )
    container: Optional[PostingFBSV4Container] = Field(
        None, description="container."
    )
    container_sort_type: Optional[str] = Field(
        None, description="Тип сортировки грузоместа."
    )
    delivering_date: Optional[str] = Field(
        None, description="Дата передачи отправления в доставку."
    )
    delivery_method: Optional[PostingFBSV4DeliveryMethod] = Field(
        None, description="delivery_method."
    )
    delivery_schema: Optional[str] = Field(
        None, description="Схема доставки."
    )
    destination_place_id: Optional[int] = Field(
        None, description="Идентификатор места назначения."
    )
    destination_place_name: Optional[str] = Field(
        None, description="Название места назначения."
    )
    external_order: Optional[PostingFBSV4ExternalOrder] = Field(
        None, description="external_order."
    )
    financial_data: Optional[PostingFBSV4FinancialData] = Field(
        None, description="financial_data."
    )
    in_process_at: Optional[str] = Field(
        None, description="Дата и время начала обработки отправления."
    )
    is_click_and_collect: Optional[bool] = Field(
        None, description="`true`, если отправление доставляется методом «Самовывоз из магазина»."
    )
    is_express: Optional[bool] = Field(
        None, description="`true`, если использовалась быстрая доставка Ozon Express."
    )
    is_multibox: Optional[bool] = Field(
        None, description="Признак, что в отправлении есть многокоробочный товар и нужно передать количество коробок для него."
    )
    is_presortable: Optional[bool] = Field(
        None, description="`true`, если товар — пересорт."
    )
    legal_info: Optional[PostingFBSV4LegalInfo] = Field(
        None, description="legal_info."
    )
    multi_box_qty: Optional[int] = Field(
        None, description="Количество коробок, в которые упакован товар."
    )
    optional: Optional[PostingFBSV4Optional] = Field(
        None, description="optional."
    )
    order_id: Optional[int] = Field(
        None, description="Идентификатор заказа, к которому относится отправление."
    )
    order_number: Optional[str] = Field(
        None, description="Номер заказа, к которому относится отправление."
    )
    parent_posting_number: Optional[str] = Field(
        None, description="Номер родительского отправления, в результате разделения которого появилось текущее."
    )
    pickup_code_verified_at: Optional[str] = Field(
        None, description="Дата и время успешной валидации кода курьера. Проверьте код курьера методом [/v1/posting/fbs/pick-up-code/verify](#operation/PostingAPI_PostingFBSPickupCodeVerify)."
    )
    posting_number: Optional[str] = Field(
        None, description="Номер отправления."
    )
    products: Optional[list[PostingFBSV4Products2]] = Field(
        None, description="Список товаров в отправлении."
    )
    prr_option: Optional[str] = Field(
        None, description="Код услуги погрузочно-разгрузочных работ."
    )
    quantum_id: Optional[int] = Field(
        None, description="Идентификатор эконом-товара."
    )
    require_blr_traceable_attrs: Optional[bool] = Field(
        None, description="`true`, если нужно заполнить атрибуты отслеживаемости."
    )
    requirements: Optional[PostingFBSV4Requirements] = Field(
        None, description="requirements."
    )
    shipment_date: Optional[str] = Field(
        None, description="Дата и время, до которой нужно собрать отправление. Показываем рекомендованное время отгрузки. По истечении этого времени начнёт применяться новый тариф, информацию о нём получите в поле `tariffication`."
    )
    shipment_date_without_delay: Optional[str] = Field(
        None, description="Дата и время отгрузки без просрочки."
    )
    status: Optional[str] = Field(
        None, description="Статус отправления."
    )
    substatus: Optional[str] = Field(
        None, description="Подстатус отправления."
    )
    tariffication: Optional[PostingFBSV4Tariffication] = Field(
        None, description="tariffication."
    )
    tariffication_steps: Optional[list[PostingFBSV4TarifficationStep]] = Field(
        None, description="Этапы тарификации."
    )
    tpl_integration_type: Optional[str] = Field(
        None, description="Тип интеграции со службой доставки."
    )
    tracking_number: Optional[str] = Field(
        None, description="Трек-номер отправления."
    )
    volume_weight: Optional[float] = Field(
        None, description="Объёмный вес товара."
    )
