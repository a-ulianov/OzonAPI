"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetProductInfoPrices"""
import datetime
from typing import Optional

from pydantic import BaseModel, Field, model_validator

from ...common.enumerations.localization import CurrencyCode
from ...common.enumerations.prices import ColorIndex
from .base import BaseRequestFilterSpec, BaseRequestCursorSpec
from ..base import BaseResponseCursor


class ProductInfoPricesFilter(BaseRequestFilterSpec):
    """Описывает схему фильтра для получения информации о ценах на товары.

    Attributes:
        offer_id (list[str]): Список offer_id (опционально, максимум 1000 значений)
        product_id (list[int]): Список product_id (опционально, максимум 1000 значений)
        visibility: (Visibility): Фильтр по видимости товара (опционально)
    """
    @model_validator(mode='after')
    def validate_total_items_count(self):
        """Проверяет, что сумма элементов по всем параметрам не превышает 1000."""
        fields_to_check = [self.offer_id, self.product_id]

        total_count = sum(len(field) for field in fields_to_check if field is not None)

        if total_count > 1000:
            raise ValueError(
                f"Общее количество идентификаторов ({total_count}) в запросе превышает максимально допустимое значение 1000."
            )

        return self


class ProductInfoPricesRequest(BaseRequestCursorSpec):
    """Описывает схему запроса на получение информации о цене товаров.

    Attributes:
        cursor (str): Указатель для выборки следующего чанка данных (опционально)
        filter: Фильтр по товарам (опционально)
        limit (int): Количество значений на странице (опционально, максимум 1000)
    """
    filter: Optional[ProductInfoPricesFilter] = Field(
        default_factory=ProductInfoPricesFilter, description="Фильтр по товарам."
    )


class ProductInfoPricesCommissions(BaseModel):
    """Информация о комиссиях.

    Attributes:
        sales_percent_fbo: Процент комиссии за продажу (FBO)
        sales_percent_fbs: Процент комиссии за продажу (FBS)
        fbo_direct_flow_trans_min_amount: Магистраль от (FBO)
        fbo_direct_flow_trans_max_amount: Магистраль до (FBO)
        fbo_deliv_to_customer_amount: Последняя миля (FBO)
        fbo_return_flow_amount: Комиссия за возврат и отмену (FBO)
        fbs_first_mile_min_amount: Минимальная комиссия за обработку отправления (FBS)
        fbs_first_mile_max_amount: Максимальная комиссия за обработку отправления (FBS)
        fbs_direct_flow_trans_min_amount: Магистраль от (FBS)
        fbs_direct_flow_trans_max_amount: Магистраль до (FBS)
        fbs_deliv_to_customer_amount: Последняя миля (FBS)
        fbs_return_flow_amount: Комиссия за возврат и отмену, обработка отправления (FBS)
    """
    sales_percent_fbo: Optional[float] = Field(
        None, description="Процент комиссии за продажу (FBO)."
    )
    sales_percent_fbs: Optional[float] = Field(
        None, description="Процент комиссии за продажу (FBS)."
    )
    fbo_direct_flow_trans_min_amount: Optional[float] = Field(
        None, description="Магистраль от (FBO)."
    )
    fbo_direct_flow_trans_max_amount: Optional[float] = Field(
        None, description="Магистраль до (FBO)."
    )
    fbo_deliv_to_customer_amount: Optional[float] = Field(
        None, description="Последняя миля (FBO)."
    )
    fbo_return_flow_amount: Optional[float] = Field(
        None, description="Комиссия за возврат и отмену (FBO)."
    )
    fbs_first_mile_min_amount: Optional[float] = Field(
        None, description="Минимальная комиссия за обработку отправления (FBS)."
    )
    fbs_first_mile_max_amount: Optional[float] = Field(
        None, description="Максимальная комиссия за обработку отправления (FBS)."
    )
    fbs_direct_flow_trans_min_amount: Optional[float] = Field(
        None, description="Магистраль от (FBS)."
    )
    fbs_direct_flow_trans_max_amount: Optional[float] = Field(
        None, description="Магистраль до (FBS)."
    )
    fbs_deliv_to_customer_amount: Optional[float] = Field(
        None, description="Последняя миля (FBS)."
    )
    fbs_return_flow_amount: Optional[float] = Field(
        None, description="Комиссия за возврат и отмену, обработка отправления (FBS)."
    )


class ProductInfoPricesAction(BaseModel):
    """Маркетинговые акции продавца.

    Attributes:
        date_from: Дата и время начала акции продавца
        date_to: Дата и время окончания акции продавца
        title: Название акции продавца
        value: Скидка по акции продавца
    """
    date_from: datetime.datetime | None = Field(
        ..., description="Дата и время начала акции продавца."
    )
    date_to: datetime.datetime | None = Field(
        ..., description="Дата и время окончания акции продавца."
    )
    title: str = Field(
        ..., description="Название акции продавца."
    )
    value: float = Field(
        ..., description="Скидка по акции продавца."
    )


class ProductInfoPricesMarketingActions(BaseModel):
    """Маркетинговые акции продавца.

    Attributes:
        actions: Скидка по акции продавца
        current_period_from: Дата и время начала текущего периода по всем действующим акциям
        current_period_to: Дата и время окончания текущего периода по всем действующим акциям
        ozon_actions_exist: Признак возможности применения акции за счёт Ozon
    """
    actions: list[ProductInfoPricesAction] = Field(
        default_factory=list, description="Скидка по акции продавца."
    )
    current_period_from: datetime.datetime | None = Field(
        ..., description="Дата и время начала текущего периода по всем действующим акциям."
    )
    current_period_to: datetime.datetime | None = Field(
        ..., description="Дата и время окончания текущего периода по всем действующим акциям."
    )
    ozon_actions_exist: bool = Field(
        ..., description="true, если к товару можно применить акцию за счёт Ozon."
    )


class ProductInfoPricesPrice(BaseModel):
    """Цена товара.

    Attributes:
        auto_action_enabled: Признак автоприменения акций
        auto_add_to_ozon_actions_list_enabled: Признак автодобавления товара в акции
        currency_code: Валюта цен
        marketing_price: Цена на товар с учётом всех акций
        marketing_seller_price: Цена на товар с учётом акций продавца
        min_price: Минимальная цена товара после применения всех скидок
        net_price: Себестоимость товара
        old_price: Цена до учёта скидок
        price: Цена товара с учётом скидок
        retail_price: Цена поставщика
        vat: Ставка НДС для товара
    """
    auto_action_enabled: bool = Field(
        ..., description="true, если автоприменение акций у товара включено."
    )
    auto_add_to_ozon_actions_list_enabled: bool = Field(
        ..., description="true, если автодобавление товара в акции включено."
    )
    currency_code: CurrencyCode = Field(
        ..., description="Валюта цен. Совпадает с валютой, которая установлена в настройках личного кабинета."
    )
    marketing_price: Optional[float] = Field(
        None, description="Цена на товар с учётом всех акций, которая будет указана на витрине Ozon, без учёта скидки по Ozon Карте."
    )
    marketing_seller_price: float = Field(
        ..., description="Цена на товар с учётом акций продавца."
    )
    min_price: float = Field(
        ..., description="Минимальная цена товара после применения всех скидок."
    )
    net_price: float = Field(
        ..., description="Себестоимость товара."
    )
    old_price: float = Field(
        ..., description="Цена до учёта скидок. На карточке товара отображается зачёркнутой."
    )
    price: float = Field(
        ..., description="Цена товара с учётом скидок — это значение показывается на карточке товара."
    )
    retail_price: float = Field(
        ..., description="Цена поставщика."
    )
    vat: float = Field(
        ..., description="Ставка НДС для товара."
    )


class ProductInfoPricesIndexData(BaseModel):
    """Базовая схема для ценовых индексов.

    Attributes:
        min_price: Минимальная цена
        min_price_currency: Валюта цены
        price_index_value: Значение индекса цены
    """
    min_price: float = Field(
        ..., description="Минимальная цена."
    )
    min_price_currency: str = Field(
        ..., description="Валюта цены."
    )
    price_index_value: float = Field(
        ..., description="Значение индекса цены."
    )


class ProductInfoPricesPriceIndexes(BaseModel):
    """Индексы цены товара.

    Attributes:
        color_index: Итоговый индекс цены товара
        external_index_data: Цена товара у конкурентов на других площадках
        ozon_index_data: Цена товара у конкурентов на Ozon
        self_marketplaces_index_data: Цена вашего товара на других площадках
    """
    color_index: Optional[ColorIndex] = Field(
        ColorIndex.WITHOUT_INDEX, description="Итоговый индекс цены товара."
    )
    external_index_data: ProductInfoPricesIndexData = Field(
        ..., description="Цена товара у конкурентов на других площадках."
    )
    ozon_index_data: ProductInfoPricesIndexData = Field(
        ..., description="Цена товара у конкурентов на Ozon."
    )
    self_marketplaces_index_data: ProductInfoPricesIndexData = Field(
        ..., description="Цена вашего товара на других площадках."
    )


class ProductInfoPricesItem(BaseModel):
    """Данные о ценах по товарной позиции.

    Attributes:
        acquiring: Максимальная комиссия за эквайринг
        commissions: Информация о комиссиях
        marketing_actions: Маркетинговые акции продавца
        offer_id: Идентификатор товара в системе продавца
        price: Цена товара
        price_indexes: Индексы цены товара
        product_id: Идентификатор товара в системе продавца
        volume_weight: Объёмный вес товара
    """
    acquiring: float = Field(
        ..., description="Максимальная комиссия за эквайринг."
    )
    commissions: ProductInfoPricesCommissions = Field(
        ..., description="Информация о комиссиях."
    )
    marketing_actions: ProductInfoPricesMarketingActions = Field(
        ..., description="Маркетинговые акции продавца."
    )
    offer_id: str = Field(
        ..., description="Идентификатор товара в системе продавца — артикул."
    )
    price: ProductInfoPricesPrice = Field(
        ..., description="Цена товара."
    )
    price_indexes: ProductInfoPricesPriceIndexes = Field(
        ..., description="Индексы цены товара."
    )
    product_id: int = Field(
        ..., description="Идентификатор товара в системе продавца — product_id."
    )
    volume_weight: float = Field(
        ..., description="Объёмный вес товара."
    )


class ProductInfoPricesResponse(BaseResponseCursor):
    """Описывает схему ответа на запрос о цене товаров.

    Attributes:
        cursor (str): Указатель для выборки следующего чанка данных
        items: Массив данных о ценах
        total (int): Общее количество результатов
    """
    items: list[ProductInfoPricesItem] = Field(
        ..., description="Массив данных о ценах."
    )