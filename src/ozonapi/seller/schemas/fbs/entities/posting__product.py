from typing import Optional

from pydantic import Field, BaseModel

from ....common.enumerations.localization import CurrencyCode


class PostingFBSProduct(BaseModel):
    """Информация о товаре в отправлении.

    Attributes:
        name: Название товара
        offer_id: Идентификатор товара в системе продавца
        price: Цена товара
        quantity: Количество товара в отправлении
        sku: Идентификатор товара в системе Ozon
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


class PostingFBSProductWithCurrencyCode(PostingFBSProduct):
    """Информация о товаре в отправлении.

    Attributes:
        name: Название товара
        offer_id: Идентификатор товара в системе продавца
        price: Цена товара
        quantity: Количество товара в отправлении
        sku: Идентификатор товара в системе Ozon
        currency_code: Валюта цен
    """
    currency_code: CurrencyCode = Field(
        ..., description="Валюта ваших цен. Совпадает с валютой, которая установлена в настройках личного кабинета."
    )


class PostingFBSProductDetailed(PostingFBSProductWithCurrencyCode):
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
