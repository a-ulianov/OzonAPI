from typing import Optional

from pydantic import Field

from ...entities.postings import PostingProductWithCurrencyCode


class PostingFBSProductDetailed(PostingProductWithCurrencyCode):
    """Детализированная информация о товаре в отправлении.

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
    is_blr_traceable: bool = Field(
        ..., description="Признак прослеживаемости товара."
    )
    is_marketplace_buyout: bool = Field(
        ..., description="Признак выкупа товара в ЕАЭС и другие страны."
    )
    imei: Optional[list[str]] = Field(
        None, description="Список IMEI мобильных устройств."
    )
