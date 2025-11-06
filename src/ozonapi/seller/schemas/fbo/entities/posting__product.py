from typing import Optional

from pydantic import Field

from ...entities.postings import PostingProductWithCurrencyCode


class PostingFBOProduct(PostingProductWithCurrencyCode):
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
