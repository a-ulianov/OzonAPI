import datetime
from typing import Optional

from pydantic import Field, BaseModel

from ..entities.common import AdditionalData
from ..entities.postings import PostingRequest, PostingAnalyticsData, Posting, PostingProductWithCurrencyCode


class PostingFBOListRequest(PostingRequest):
    """Описывает схему запроса на получение информации об отправлениях FBO.

    Attributes:
        dir: Направление сортировки
        filter: Фильтр выборки
        limit: Количество значений в ответе
        offset: Количество элементов, которое будет пропущено в ответе
        with_: Дополнительные поля, которые нужно добавить в ответ
        translit: Если включена транслитерация адреса из кириллицы в латиницу — true
    """
    translit: Optional[bool] = Field(
        False
    )


class PostingFBOListAnalyticsData(PostingAnalyticsData):
    """Данные аналитики.

    Attributes:
        city: Город доставки
        delivery_type: Способ доставки
        is_legal: Признак юридического лица
        is_premium: Наличие подписки Premium
        payment_type_group_name: Способ оплаты
        region: Регион доставки
        warehouse_id: Идентификатор склада
        warehouse_name: Название склада отправки заказа
    """
    warehouse_name: Optional[str] = Field(
        None, description="Название склада отправки заказа."
    )


class PostingFBOListProduct(PostingProductWithCurrencyCode):
    """Информация о товаре в отправлении.

    Attributes:
        digital_codes: Коды активации для услуг и цифровых товаров
        name: Название товара
        offer_id: Идентификатор товара в системе продавца
        currency_code: Валюта цен
        price: Цена товара
        is_marketplace_buyout: Признак выкупа товара в ЕАЭС и другие страны
        quantity: Количество товара в отправлении
        sku: Идентификатор товара в системе Ozon
    """
    digital_codes: Optional[list[str]] = Field(
        default_factory=list, description="Коды активации для услуг и цифровых товаров."
    )
    is_marketplace_buyout: Optional[bool] = Field(
        None, description="Признак выкупа товара в ЕАЭС и другие страны."
    )


class PostingFBOListPosting(Posting):
    """Описывает отправление.

    Attributes:
        additional_data: Дополнительная информация
        analytics_data: Данные аналитики
        cancel_reason_id: Идентификатор причины отмены отправления
        created_at: Дата и время создания отправления
        financial_data: Финансовые данные
        in_process_at: Дата и время начала обработки отправления
        legal_info: Юридическая информация о покупателе
        order_id: Идентификатор заказа, к которому относится отправление
        order_number: Номер заказа, к которому относится отправление
        posting_number: Номер отправления
        products: Список товаров в отправлении
        status: Статус отправления
    """
    additional_data: Optional[list[AdditionalData]] = Field(
        default_factory=list, description="Дополнительная информация."
    )
    analytics_data: Optional[PostingFBOListAnalyticsData] = Field(
        None, description="Данные аналитики."
    )
    cancel_reason_id: Optional[int] = Field(
        None, description="Идентификатор причины отмены отправления."
    )
    created_at: Optional[datetime.datetime] = Field(
        None, description="Дата и время создания отправления."
    )
    products: Optional[list[PostingFBOListProduct]] = Field(
        default_factory=list, description="Список товаров в отправлении."
    )

class PostingFBOListResponse(BaseModel):
    """Описывает схему ответа на запрос на получение информации об отправлениях FBO.

    Attributes:
        result: Массив отправлений
    """
    result: Optional[list[PostingFBOListPosting]] = Field(
        default_factory=list, description="Массив отправлений."
    )